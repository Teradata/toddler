from openai import OpenAI
from dotenv import load_dotenv
import json
import logging
from typing import Any

logging.basicConfig(filename='logs/log.txt', filemode='a', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


load_dotenv()
client = OpenAI()

# LLM interactions
def base(system_prompt, user_prompt):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      system_prompt,
      user_prompt
    ])
  return(completion.choices[0].message)

def validate_chunk(chunk: dict) -> bool:
  return 'heading' in chunk and 'text' in chunk

def request_questions(processing_chunk: dict) -> Any:
  if validate_chunk(processing_chunk):
    text = processing_chunk['text']
    heading = processing_chunk['heading']
    system_prompt = {"role": "system", "content": "You are analyzing technical documentation to generate relevant technical questions and answers based on the content of the prompt"}
    prompt_text = f'''
    from the following text: {text}. That is found within the context of the heading {heading} generate a set of questions that can be used to test the reader\'s understanding of the text and their corresponding answers, 
    the questions and the answers should be based on the provided text. 
    The response should be a list of objects, each object on the list should have two keys with an individual value each,
    one key should be "question" the other key should be "answer",
    the format of the respons should be JSON, please avoid beutifying the JSON it should be a single string of texts.
    '''
    user_prompt = {"role": "user", "content": f"{prompt_text}"}
    result = base(system_prompt, user_prompt).content
    return result
  else:
    raise ValueError("Chunk is not valid")
  
# Response processing

def single_chunk_processing(chunk: dict) -> str:
    response = request_questions(chunk)
    try:
      processed_response = json.loads(response)
    except:
      logging.error(f"Failed to process chunk: {chunk}")
    return processed_response 

def bulk_chunk_processing(chunks: list) -> list:
    questions = []
    for chunk in chunks:
        current_response = single_chunk_processing(chunk)
        questions.extend(current_response)
    return questions