import unittest
from unittest.mock import patch
from toddler.llm_requests import validate_chunk, request_questions

class TestLLMRequests(unittest.TestCase):

    def test_validate_chunk_valid(self):
        chunk = {'heading': 'Test Heading', 'text': 'Test Text'}
        self.assertTrue(validate_chunk(chunk))

    def test_validate_chunk_no_heading(self):
        chunk = {'text': 'Test Text'}
        self.assertFalse(validate_chunk(chunk))

    def test_validate_chunk_no_text(self):
        chunk = {'heading': 'Test Heading'}
        self.assertFalse(validate_chunk(chunk))

    def test_validate_chunk_empty(self):
        chunk = {}
        self.assertFalse(validate_chunk(chunk))

    @patch('llm_requests.client.chat.completions.create')
    def test_request_questions_valid(self, mock_create):
        mock_create.return_value = {
            "choices": [{"message": '{"question": "What is X?", "answer": "X is Y."}'}]
        }
        chunk = {'heading': 'Test Heading', 'text': 'Test Text'}
        result = request_questions(chunk)
        self.assertIn('question', result)
        self.assertIn('answer', result)

    @patch('llm_requests.client.chat.completions.create')
    def test_request_questions_invalid_chunk(self, mock_create):
        chunk = {'heading': 'Only Heading'}
        try:
            result = request_questions(chunk)
        except:
            self.assertRaises(ValueError)
        

if __name__ == '__main__':
    unittest.main()