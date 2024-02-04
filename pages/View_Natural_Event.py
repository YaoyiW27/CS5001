'''
Yaoyi Wang
CS 5001, Fall 2023
Final project -- NASA's open API

This is Natural Event viewing Page Module.
'''
import streamlit as st
from models.NaturalEvent import NaturalEvent

# Initialize and fetch data from the NaturalEvent class
natural_event = NaturalEvent()
natural_event.fetch_events()

# Display the fetched natural events on the page
if natural_event.error_message:
    st.error(natural_event.error_message)
elif natural_event.events:
    st.header('Natural Events 🌋')
    for event in natural_event.events:
        event_title = event.get('title', 'No Title')
        st.subheader(event_title)

        # Safely access 'geometries' and 'categories'
        geometries = event.get('geometries', [{}]) 
        # Attempts to fetch the 'geometries' data from each event, defaulting to [{}] if not present
        if geometries:
            st.write('Date:', geometries[0].get('date', 'No Date'))

        categories = event.get('categories', [{}])
        if categories:
            st.write('Type:', categories[0].get('title', 'No Type'))

        # Provide direct links to the source URLs
        sources = event.get('sources', [])
        if sources:
            for source in sources:
                source_url = source.get('url', '#')
                source_title = source.get('id', 'Source')
                st.markdown(f"[{source_title}]({source_url})")
        else:
            st.markdown("No source links available.")
else:
    st.write("No natural events data available.")
