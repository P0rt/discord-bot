import unittest
from unittest.mock import patch, Mock
from src.bot.bot import send_to_api

class TestBotFunctions(unittest.TestCase):

    @patch('src.bot.bot.requests.get')
    def test_send_to_api_valid_response(self, mock_get):
        # Имитируем успешный ответ API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Test Content"
                    }
                }
            ]
        }
        
        mock_get.return_value = mock_response

        response = send_to_api("test message")
        self.assertEqual(response, "Test Content")

    @patch('src.bot.bot.requests.get')
    def test_send_to_api_invalid_response(self, mock_get):
        # Имитируем неудачный ответ API
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = requests.HTTPError()

        mock_get.return_value = mock_response

        response = send_to_api("test message")
        self.assertIn("HTTP error occurred", response)

    @patch('src.bot.bot.requests.get')
    def test_send_to_api_unexpected_response(self, mock_get):
        # Имитируем неожиданный формат ответа API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        
        mock_get.return_value = mock_response

        response = send_to_api("test message")
        self.assertIn("Unexpected API response", response)


if __name__ == '__main__':
    unittest.main()
