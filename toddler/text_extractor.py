import pymupdf4llm
import pathlib

def extract_pdf_md(path: str, initial_page: int, final_page: int) -> str:
    # Validate page numbers
    if initial_page < 1 or final_page < 1:
        raise ValueError("Initial and final page must be greater than 0")
    if initial_page > final_page:
        raise ValueError("Initial page must be less than or equal to final page")
    
    # Validate path
    pdf_path = pathlib.Path(path)
    if not pdf_path.exists():
        raise FileNotFoundError("File not found")
    if not pdf_path.is_file():
        raise ValueError("Path must be a file")
    if not path.endswith(".pdf"):
        raise ValueError("File must be a PDF")
    
    # Open the PDF to check total pages and adjust page numbers if necessary
    try:
        md_text = pymupdf4llm.to_markdown(path, pages=list(range(initial_page - 1, final_page)), page_chunks=False)
    except Exception as e:
        raise RuntimeError(f"Failed to extract PDF: {e}")    
    
    return md_text

def is_chunk_empty(chunk: dict) -> bool:
    return not chunk['heading'] and not chunk['text']

def find_lowest_level_heading(markdown_text: str) -> int:
    lines = markdown_text.split('\n')
    lowest_level = 0
    for line in lines:
        stripped_line = line.lstrip() 
        if stripped_line.startswith('#'):
            level = len(stripped_line) - len(stripped_line.lstrip('#'))
            if level > lowest_level:
                lowest_level = level
    return lowest_level 

def split_markdown_by_headings_multilevel(markdown_text: str, final_heading_marker: str) -> list:
    lines = markdown_text.split('\n')
    chunks = []
    current_chunk = {'heading': '', 'text': '', 'chunk_length': 0}
    is_first_chunk = True
    current_text = []
    line_count = 0

    for line in lines:
        # Determine if line is a heading
        # Determine if the heading level should taking into consideration
        # If line is heading that should be taken into consideration, close previous chunk if any and not empty, update heading and start new chunk
        if len(line) - len(line.lstrip('#')) > 0 and len(line) - len(line.lstrip('#')) <= len(final_heading_marker):
            if not is_first_chunk and not is_chunk_empty(current_chunk):
                current_chunk['text'] = '\n'.join(current_text)
                current_chunk['chunk_length'] = len(current_chunk['text'])
                chunks.append(current_chunk)
                current_text = []
                current_chunk = {'heading': '', 'text': ''}
            current_chunk['heading'] = line.strip('#').strip()
        else:
            current_text.append(line)
            if is_first_chunk:
                is_first_chunk = False       
        line_count += 1
    
    # Add the last chunk if it exists
    if current_chunk['text'] or current_chunk['heading']:
        current_chunk['text'] = '\n'.join(current_text)
        current_chunk['chunk_length'] = len(current_chunk['text'])
        chunks.append(current_chunk)
    
    # If no headings were found, treat the entire text as a single chunk
    if len(chunks) == 0 and len(current_text) > 0:
        current_chunk['heading'] = ''
        current_chunk['text'] = '\n'.join(current_text)
        current_chunk['chunk_length'] = len(current_chunk['text'])
        chunks.append(current_chunk)
    return chunks

def text_extractor(path: str, initial_page: int, final_page: int) -> dict:
    md_content = extract_pdf_md(path=path, initial_page=initial_page, final_page=final_page)
    lowest_level_heading = find_lowest_level_heading(md_content)
    (final_heading_marker := '#' * lowest_level_heading) if lowest_level_heading > 0 else (final_heading_marker := '' )
    chunks = split_markdown_by_headings_multilevel(md_content, final_heading_marker=final_heading_marker)
    longest_chunk_length = max(chunks, key=lambda x: x['chunk_length'])['chunk_length']
    result = {'metadata':{'chunk_number': len(chunks),'lowest_heading':final_heading_marker,'longest_chung_length':longest_chunk_length}, "chunks": chunks}
    return result