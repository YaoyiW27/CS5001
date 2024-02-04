'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is a class to interact with NASA's Earth Polychromatic Imaging Camera (EPIC) API.
'''
import requests


class DailyEarthView:
    '''
    Daily Earth View model
    '''

    base_url = "https://api.nasa.gov/EPIC/api"

    def __init__(self, api_key="DEMO_KEY"):
        '''
        This method initializes the DailyEarthView object with a default or provided API key.
        If no API key is provided when an instance of the class is created, it will default to using "DEMO_KEY"
        The API key is used for authenticating requests to the NASA EPIC API.
        '''
        self.api_key = api_key

    def fetch_images(self, date=None, image_type='natural'):
        '''
        Retrieves Earth images from NASA's EPIC (Earth Polychromatic Imaging Camera) API.

        Parameters:
        - date (optional, str): A string specifying the date for which images should be fetched. 
        The date should be in 'YYYY-MM-DD' format. If no date is provided, the method fetches 
        the most recent images available.
        - image_type (optional, str): A string that specifies the type of images to retrieve. 
        Possible values include 'natural' for natural color images, 'enhanced' for images 
        with enhanced color, among others. Defaults to 'natural' if not specified.

        The method constructs an API request URL using the provided date and image type. 
        It then makes an HTTP GET request to the NASA EPIC API.

        Returns a list of image data in JSON format if the request is successful.

        Raises an exception if the API request fails.
        '''
        date_endpoint = f"/{image_type}/date/{date}" if date else f"/{image_type}"
        # The structure x if condition else y is a ternary operator in Python.
        response = requests.get(f"{self.base_url}{date_endpoint}", params={'api_key': self.api_key})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch EPIC images: {response.status_code}")
