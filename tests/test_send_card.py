import unittest
from unittest.mock import patch, MagicMock
from teams_alert.send_card import TeamsAlert
from teams_alert.templates import gen_card_no_person, gen_card_to_person
import json

class TestTeamsAlert(unittest.TestCase):
    def setUp(self):
        self.url = "https://example.com/webhook"
        self.teams_alert = TeamsAlert(self.url)

    def test_init(self):
        self.assertEqual(self.teams_alert.url, self.url)

    @patch('teams_alert.send_card.requests.request')
    def test_send_message(self, mock_request):

        mock_response = MagicMock(status_code=200)
        mock_request.return_value = mock_response

        self.teams_alert.title = "Test Title"
        self.teams_alert.message = "Test Message"

        response = self.teams_alert._send_message()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(mock_request.call_args[0][0], "POST")
        self.assertEqual(mock_request.call_args[0][1], self.url)
        self.assertEqual(mock_request.call_args[1]['headers'], {'Content-Type': 'application/json'})

        expected_payload = gen_card_no_person("Test Title", "Test Message")
        self.assert_json_equal(mock_request.call_args[1]['data'], expected_payload)

    def assert_json_equal(self, json1, json2):
        """Assert that two JSON objects are equal."""
        self.assertEqual(json.loads(json1) if isinstance(json1, str) else json1,
                         json.loads(json2) if isinstance(json2, str) else json2)

    @patch('teams_alert.send_card.requests.request')
    def test_send_message_with_attention(self, mock_request):
        mock_response = MagicMock(status_code=200)
        mock_request.return_value = mock_response

        self.teams_alert.title = "Test Title"
        self.teams_alert.message = "Test Message"
        self.teams_alert.attention = "user@example.com"

        response = self.teams_alert._send_message_with_attention()

        self.assertEqual(response.status_code, 200)

        self.assertEqual(mock_request.call_args[0][0], "POST")
        self.assertEqual(mock_request.call_args[0][1], self.url)
        self.assertEqual(mock_request.call_args[1]['headers'], {'Content-Type': 'application/json'})

        expected_payload = gen_card_to_person("Test Title", "Test Message", "user@example.com")

        self.assert_json_equal(mock_request.call_args[1]['data'], expected_payload)

if __name__ == '__main__':
    unittest.main()