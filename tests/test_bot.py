import unittest
from unittest.mock import patch
from src.bot.bot import send_to_api

class TestBotMethods(unittest.TestCase):

    @patch('bot.requests.get')
    @patch('bot.os.environ.get', return_value="TEST_DISCORD_TOKEN")
    def test_send_to_api_valid_response(self, mock_get, mock_os_environ_get):
        mock_response = type('', (), {})()
        mock_response.json = lambda: {
            "choices": [
                {"message": {"content": "test message"}}
            ]
        }
        mock_response.raise_for_status = lambda: None
        mock_get.return_value = mock_response

        message = "hello"
        response = send_to_api(message)
        self.assertEqual(response, "test message")

    @patch('bot.requests.get')
    @patch('bot.os.environ.get', return_value="TEST_DISCORD_TOKEN")
    def test_send_to_api_invalid_response(self, mock_get, mock_os_environ_get):
        mock_response = type('', (), {})()
        mock_response.json = lambda: {}
        mock_response.raise_for_status = lambda: None
        mock_get.return_value = mock_response

        message = "hello"
        response = send_to_api(message)
        self.assertIn("Unexpected API response:", response)

if __name__ == '__main__':
    unittest.main()
