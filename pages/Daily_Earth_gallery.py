'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is EPIC Daily Earth Gallery Page Module.
'''
import streamlit as st
from models.DailyEarthView import DailyEarthView


def display_earth_gallery_page():
    st.title('EPIC Daily Earth Gallery 🌍')

    # Define the image type
    image_type = 'natural'  

    # Create an instance of DailyEarthView
    epic_viewer = DailyEarthView()

    # Fetch the list of recent images
    images = epic_viewer.fetch_images()

    # Display images in a gallery format
    if images:
        cols = st.columns(3)  # Creates a layout with three columns on the Streamlit app page
        for idx, image in enumerate(images):
            with cols[idx % 3]:  # This will return to the first column after every 3 images
                date = image['date'].split(' ')[0]  # Assuming the date is the first part of a space-separated string
                image_url = f"https://epic.gsfc.nasa.gov/archive/{image_type}/{date.replace('-', '/')}/png/{image['image']}.png"
                st.image(image_url, width=200, caption=image.get('caption', ''))
                # Displays the image in the Streamlit app with a width of 200 pixels
                # If a caption is available in the image data, it's displayed; otherwise, an empty string is used as the caption
                st.write(image['date'])
    else:
        st.error("No images available.")


display_earth_gallery_page()
