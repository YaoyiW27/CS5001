'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is unit test for AstronomyPicture class.
'''
import unittest
import requests
from unittest.mock import Mock, patch
from AstronomyPicture import AstronomyPicture


class TestAstronomyPicture(unittest.TestCase):

    def setUp(self):
        self.apod = AstronomyPicture()

    @patch('requests.get')
    def test_fetch_successful(self, mock_get):
        # Mock the requests.get method to return a successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'url': 'https://example.com/image.jpg',
            'explanation': 'Astronomy picture explanation',
            'title': 'Astronomy picture title'
        }
        mock_get.return_value = mock_response

        # Call the fetch method
        self.apod.fetch()

        # Assert that attributes are set correctly
        self.assertEqual(self.apod.image_url, 'https://example.com/image.jpg')
        self.assertEqual(self.apod.explanation, 'Astronomy picture explanation')
        self.assertEqual(self.apod.title, 'Astronomy picture title')
        self.assertIsNone(self.apod.error_message)

    @patch('requests.get')
    def test_fetch_unsuccessful(self, mock_get):
        # Mock the requests.get method to return an unsuccessful response
        mock_response = Mock()
        mock_response.status_code = 404 # Not Found
        mock_get.return_value = mock_response

        # Call the fetch method
        self.apod.fetch()

        # Assert that error_message is set correctly
        self.assertEqual(self.apod.error_message, 'Error fetching data: HTTP status code 404')
        self.assertIsNone(self.apod.image_url)
        self.assertIsNone(self.apod.explanation)
        self.assertIsNone(self.apod.title)

    @patch('requests.get', side_effect=requests.exceptions.RequestException('Network error'))
    def test_fetch_network_error(self, mock_get):
        # Mock the requests.get method to raise a network error
        # This simulates a network-related issue
        mock_get.side_effect = requests.exceptions.RequestException('Network error')

        # Call the fetch method
        self.apod.fetch()

        # Assert that error_message is set correctly
        self.assertEqual(self.apod.error_message, 'Error fetching data: Network error')
        self.assertIsNone(self.apod.image_url)
        self.assertIsNone(self.apod.explanation)
        self.assertIsNone(self.apod.title)


if __name__ == '__main__':
    unittest.main()
