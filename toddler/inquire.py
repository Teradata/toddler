import argparse
from llm_requests import bulk_chunk_processing
from text_extractor import text_extractor
import json

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Input PDF file path, initial and final page numbers, and output file name.')

    # Add arguments
    parser.add_argument('input_path', type=str, help='Path to the input PDF file')
    parser.add_argument('initial_page', type=int, help='Initial page number to process')
    parser.add_argument('final_page', type=int, help='Final page number to process')
    parser.add_argument('output_name', type=str, help='Name of the output file without extension')

    # Parse arguments
    args = parser.parse_args()

    # Extract text and process chunks
    test_data = text_extractor(path=args.input_path, initial_page=args.initial_page, final_page=args.final_page)
    questions = bulk_chunk_processing(test_data['chunks'])

    # Save to JSON
    with open(f'outputs/{args.output_name}.json', 'w') as outfile:
        json.dump(questions, outfile)

if __name__ == "__main__":
    main()

# main.py "./test_data/teradata-analytics.pdf" 27 40 "questions_output" 