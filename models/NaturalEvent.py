'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is a class to interact with NASA's Earth Observatory Natural Event Tracker (EONET) API.
'''
import requests


class NaturalEvent:
    '''
    Earth Observatory Natural Event Tracker (EONET) model
    '''

    base_url = "https://eonet.gsfc.nasa.gov/api/v3/events"

    def __init__(self):
        '''
        Initializes the attributes to store information about natural events and potential error messages.
        '''
        self.events = None
        self.error_message = None

    def fetch_events(self, params=None):
        '''
        Fetches the latest natural events from EONET
        The method sends a request to the EONET API and updates the 'events' attribute with the response.
        In case of non-successful responses or network issues, it sets an error message and returns an empty list.
        '''
        try:
            response = requests.get(self.base_url, params=params) # params=params passes any additional parameters to the API request
            if response.status_code == 200:
                self.events = response.json().get('events', [])
            else:
                # Handle non-successful status codes
                self.error_message = f"Error fetching events: HTTP status code {response.status_code}"
                self.events = []
        except requests.exceptions.RequestException as e:
            # Handle other request issues like network problems
            self.error_message = f"Error fetching events: {e}"
            return []  # Return an empty list in case of an exception
