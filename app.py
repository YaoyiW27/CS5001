import streamlit as st
from pages.Daily_Earth_gallery import DailyEarthView
from pages.Display_Astronomy_Picture_of_the_Day import AstronomyPicture
from pages.Search_Astronomy_Picture_of_the_Day import AstronomyPicture
from pages.View_Natural_Event import NaturalEvent
from datetime import datetime

st.title('NASA: Exploring the Outer Space and Earth 🪐')

st.markdown("Welcome to NASA's Visual Universe 🌌")
st.markdown("Explore the vastness of space with NASA's open APIs! ")

st.header('Astronomy Picture of the Day 🔭')

apod = AstronomyPicture()
apod.fetch()

today = datetime.now().strftime("%Y-%m-%d")
st.write(f"{today}")

if apod.image_url:
    st.image(apod.image_url, caption=apod.title)
    st.markdown(f"**Explanation:** {apod.explanation}")
else:
    st.write("No data available for the Astronomy Picture of the Day.")


st.header('Daily Earth Gallery 🌍')

def display_earth_gallery_page():
    image_type = 'natural'  
    epic_viewer = DailyEarthView()
    images = epic_viewer.fetch_images()

    if images:
        cols = st.columns(3)  
        for idx, image in enumerate(images):
            with cols[idx % 3]:  
                date = image['date'].split(' ')[0]  
                image_url = f"https://epic.gsfc.nasa.gov/archive/{image_type}/{date.replace('-', '/')}/png/{image['image']}.png"
                st.image(image_url, width=200, caption=image.get('caption', ''))
                st.write(image['date'])
    else:
        st.error("No images available.")


display_earth_gallery_page()


st.header('Search Astronomy Picture of the Day 🔍')

date = st.text_input("Enter Date (YYYY-MM-DD):")

if st.button('Search'):
    apod = AstronomyPicture(date)
    apod.fetch()

    if apod.image_url:
        st.image(apod.image_url, caption=apod.title)
        st.markdown(f"**Explanation:** {apod.explanation}")
    else:
        st.write("No data available for the specified date.")


st.header('Natural Events')
natural_event = NaturalEvent()
natural_event.fetch_events()
st.markdown('Due to some NASA data being lost, the links to the following natural events have some data that is lost and cannot be opened.')
if natural_event.error_message:
    st.error(natural_event.error_message)
elif natural_event.events:
    st.header('Natural Events 🌋')
    for event in natural_event.events:
        event_title = event.get('title', 'No Title')
        st.subheader(event_title)

        geometries = event.get('geometries', [{}]) 

        if geometries:
            st.write('Date:', geometries[0].get('date', 'No Date'))

        categories = event.get('categories', [{}])
        if categories:
            st.write('Type:', categories[0].get('title', 'No Type'))

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
