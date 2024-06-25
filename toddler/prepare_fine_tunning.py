import argparse
from llm_requests import bulk_chunk_processing
from text_extractor import text_extractor
import json
import logging

logging.basicConfig(filename='logs/log.txt', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_input_structure(input_data):
    question_index = 0
    for pair in input_data:
        if 'question' not in pair or 'answer' not in pair.keys():
            logging.error(f"Question-answer {pair} at index {question_index} is missing 'question' or 'answer' key.")
            return False
        else:
            return True

def convert_qa_to_chat(input_file, output_file, system_message):
    # Read the input JSON file
    question_index = 0
    
    with open(input_file, 'r') as f:
        qa_pairs = json.load(f)
    
    content_is_valid = check_input_structure(qa_pairs)
    if not content_is_valid:
        raise ValueError("Input data is not in the expected format. Each object in the input data should have a 'question' and 'answer' key.")

    # Open the output file
    with open(f'./outputs/{output_file}.jsonl', 'w') as f:
        # Iterate over each question-answer pair
        for pair in qa_pairs:
            # Prepare the chat message structure
            #print(f'processing pair {pair} at index {question_index}')
            try:
                chat_message = {
                    "messages": [
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": pair["question"]},
                        {"role": "assistant", "content": pair["answer"]}
                    ]
                }
                # Write the chat message to the output file as a JSONL line
                f.write(json.dumps(chat_message) + '\n')

            except Exception as e:
                logging.error(f"Failed to process question-answer {pair} at index {question_index}: {e}")
            question_index += 1

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Convert QA pairs from a JSON file to a chat format JSONL file.')

    # Add arguments
    parser.add_argument('input_file', type=str, help='Path to the input JSON file containing QA pairs.')
    parser.add_argument('output_file', type=str, help='Name of the output JSONL file without extension.')
    parser.add_argument('system_message', type=str, help='System message to include in each chat.')

    # Parse arguments
    args = parser.parse_args()

    # Convert QA to chat format
    convert_qa_to_chat(args.input_file, args.output_file, args.system_message)

if __name__ == "__main__":
    main()



