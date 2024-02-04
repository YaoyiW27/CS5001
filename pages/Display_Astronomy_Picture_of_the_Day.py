'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is Display Page: Astronomy Picture of the Day Module.
'''
import streamlit as st
from models.AstronomyPicture import AstronomyPicture
from datetime import datetime

# Display APOD page
apod = AstronomyPicture()
apod.fetch()

st.header('Astronomy Picture of the Day 🔭')

# Displaying today's date at the top of the page
today = datetime.now().strftime("%Y-%m-%d")
st.write(f"{today}")

# Displaying the Astronomy Picture of the Day if available
if apod.image_url:
    st.image(apod.image_url, caption=apod.title)
    st.markdown(f"**Explanation:** {apod.explanation}")
else:
    st.write("No data available for the Astronomy Picture of the Day.")
