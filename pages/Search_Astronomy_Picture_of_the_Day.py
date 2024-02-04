'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is Search Page: Astronomy Picture of the Day Module.
'''
import streamlit as st
from models.AstronomyPicture import AstronomyPicture

# Display the search page for Astronomy Picture of the Day (APOD)
st.header('Search Astronomy Picture of the Day 🔍')

# User input for date
date = st.text_input("Enter Date (YYYY-MM-DD):")

# Search functionality
if st.button('Search'):
    # Fetch APOD for the specified date
    apod = AstronomyPicture(date)
    apod.fetch()

    # Display the APOD image and explanation if available
    if apod.image_url:
        st.image(apod.image_url, caption=apod.title)
        st.markdown(f"**Explanation:** {apod.explanation}")
    else:
        st.write("No data available for the specified date.")
