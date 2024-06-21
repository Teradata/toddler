import pytest
from unittest.mock import patch
from toddler.text_extractor import text_extractor

# Sample markdown content to simulate PDF extraction
sample_md_content = """
# Heading 1
Text under heading 1
## Heading 1.1
Text under heading 1.1
"""

def mock_extract_pdf_md(path, initial_page, final_page):
    return sample_md_content

@pytest.fixture
def pdf_path():
    return "./test_data/teradata-analytics.pdf"

@patch('text_extractor.extract_pdf_md', side_effect=mock_extract_pdf_md)
def test_text_extractor_structure(mock_extract, pdf_path):
    result = text_extractor(pdf_path, 1, 1)
    assert 'metadata' in result
    assert 'chunks' in result
    assert isinstance(result['chunks'], list)
    assert 'chunk_number' in result['metadata']
    assert 'lowest_heading' in result['metadata']
    assert 'longest_chung_length' in result['metadata']  # Note: Should correct the typo to 'longest_chunk_length'

@patch('text_extractor.extract_pdf_md', side_effect=mock_extract_pdf_md)
def test_text_extractor_content(mock_extract, pdf_path):
    result = text_extractor(pdf_path, 1, 1)
    assert len(result['chunks']) == 1  
    assert result['metadata']['chunk_number'] == 1
    

