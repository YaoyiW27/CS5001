'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is unit test for NaturalEvent class.
'''
import unittest
from unittest.mock import patch
from NaturalEvent import NaturalEvent


class TestNaturalEvent(unittest.TestCase):

    @patch('requests.get')
    def test_get_events_success(self, mock_get):
        # Mock a successful response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"events": [{"event1_key": "event1_value"}, {"event2_key": "event2_value"}]}
        mock_get.return_value = mock_response

        natural_event = NaturalEvent()
        events = natural_event.fetch_events()
        events = natural_event.events

        self.assertEqual(events, [{"event1_key": "event1_value"}, {"event2_key": "event2_value"}])
        mock_get.assert_called_once_with('https://eonet.gsfc.nasa.gov/api/v3/events', params=None)

    @patch('requests.get')
    def test_get_events_failure(self, mock_get):
        # Mock a failure response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500 #  Internal Server Error
        mock_get.return_value = mock_response

        natural_event = NaturalEvent()
        events = natural_event.fetch_events()
        events = natural_event.events

        self.assertEqual(events, [])
        mock_get.assert_called_once_with('https://eonet.gsfc.nasa.gov/api/v3/events', params=None)


if __name__ == '__main__':
    unittest.main()
