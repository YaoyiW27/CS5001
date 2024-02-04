'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is unit test for DailyEarthView class.
'''
import unittest
from unittest.mock import patch
from DailyEarthView import DailyEarthView


class TestDailyEarthView(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_images_success(self, mock_get):
        # Mock a successful response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{'image1_key': 'image1_value'}, {'image2_key': 'image2_value'}]
        mock_get.return_value = mock_response

        daily_earth_view = DailyEarthView(api_key='RoobzgT212alSngmNTi8WqyzxqGAGFc4A3hlhREt')
        images = daily_earth_view.fetch_images(date='2023-11-28', image_type='natural')

        self.assertEqual(images, [{'image1_key': 'image1_value'}, {'image2_key': 'image2_value'}])
        mock_get.assert_called_once_with('https://api.nasa.gov/EPIC/api/natural/date/2023-11-28', params={'api_key': 'RoobzgT212alSngmNTi8WqyzxqGAGFc4A3hlhREt'})

    @patch('requests.get')
    def test_fetch_images_failure(self, mock_get):
        # Mock a failure response
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500 # Internal Server Error
        mock_get.return_value = mock_response

        daily_earth_view = DailyEarthView(api_key='RoobzgT212alSngmNTi8WqyzxqGAGFc4A3hlhREt')
 
        with self.assertRaises(Exception) as context:
            daily_earth_view.fetch_images(date='2023-11-28', image_type='natural')

        self.assertEqual(str(context.exception), "Failed to fetch EPIC images: 500")
        mock_get.assert_called_once_with(
            'https://api.nasa.gov/EPIC/api/natural/date/2023-11-28',
            params={'api_key': 'RoobzgT212alSngmNTi8WqyzxqGAGFc4A3hlhREt'}
        )


if __name__ == '__main__':
    unittest.main()
