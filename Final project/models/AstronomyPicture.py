'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is a class to interact with NASA's Astronomy Picture of the Day (APOD) API.
'''
import requests


class AstronomyPicture:
    '''
    Astronomy Picture of the Day model
    '''

    base_url = "https://api.nasa.gov/planetary/apod"
    api_key = "RoobzgT212alSngmNTi8WqyzxqGAGFc4A3hlhREt"

    def __init__(self, date=None):
        '''
        Constructor for the AstronomyPicture class.
        This method initializes a new instance of the AstronomyPicture object, setting up 
        the initial state of the object with various attributes and optional date parameter.
        '''
        self.date = date
        self.image_url = None
        self.explanation = None
        self.title = None
        self.error_message = None

    def fetch(self):
        '''
        Fetches data from the NASA Astronomy Picture of the Day (APOD) API.

        This method sends an HTTP GET request to the APOD API using the base URL and API key 
        stored in the class. It uses the 'date' attribute of the instance to fetch the APOD 
        for a specific date, if provided. If no date is specified, the latest APOD is retrieved.

        The method updates the instance's attributes based on the API response:
        - self.image_url
        - self.explanation
        - self.title

        No return value. The method modifies the instance attributes directly.
        '''
        params = {'api_key': self.api_key}
        if self.date:
            params['date'] = self.date
            # This line adds another key-value pair to the params dictionary.
            # 'date' is the key, and self.date is the value.

        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                # Handle successful status code
                data = response.json()
                self.image_url = data.get('url')
                self.explanation = data.get('explanation')
                self.title = data.get('title')
            else:
                # Handle non-successful status codes
                self.error_message = f"Error fetching data: HTTP status code {response.status_code}"
        except requests.exceptions.RequestException as e:
            # Handle other request issues like network problems
            self.error_message = f"Error fetching data: {e}"
