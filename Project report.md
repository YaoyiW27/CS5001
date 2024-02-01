# CS 5001 Final Project Report - Yaoyi Wang

## 1. Project summary

This web application leverages NASA's Open APIs to bring space exploration and astronomical wonders closer to the public. This platform will captivate users with the Astronomy Picture of the Day, offering images, explanations, and dates, while also providing a Daily Earth Photos Gallery for immersive exploration. Users can search for specific Astronomy Pictures, and experience the oddity of earth through the View Natural Event feature.


## 2. Description of the REST API(s) 

### REST API: Astronomy Picture of the Day (APOD)

**URL:** https://api.nasa.gov/

**Documentation:** https://api.nasa.gov/planetary/apod

**Description:** I will fetch data about astronomy picture of the date to display the image along with relevant information. Additionally, I will use this API to implement a search feature that enables users to find astronomy picture of a specific day.

#### Endpoints:

*`/apod` - get NASA's Astronomy Picture of the Day 

*`/apod/:explanation` - get an explanation of the picture

*`/apod/:date` - get a date of the picture

### REST API: Earth Polychromatic Imaging Camera (EPIC)

**URL:** https://epic.gsfc.nasa.gov/

**Documentation:** https://epic.gsfc.nasa.gov/about/api

**Description:** I will fetch photos of NASA's daily imagery captured by DSCOVR's Earth Polychromatic Imaging Camera (EPIC) instrument, making it readily accessible to the public. 

#### Endpoints:

*`/natural/date/YYYY-MM-DD` - get image of natural type 

*`/enhanced/date/YYYY-MM-DD` - get image of enhanced type 

*`/aerosol/date/YYYY-MM-DD` - get image of aerosol type 

### REST API: Earth Observatory Natural Event Tracker (EONET) 

**URL:** https://eonet.gsfc.nasa.gov/api/v3/events

**Documentation:** https://eonet.gsfc.nasa.gov/docs/v3

**Description:** I will retrieve information about natural events from NASA's Earth Observatory Natural Event Tracker (EONET) API. Users can access data on various natural events such as wildfires, earthquakes, hurricanes, and more. 

#### Endpoints:

*`/events` - Get a list of all natural events in the EONET database.

*`/tyepes` - Get a list of event categories, each containing related natural events.

*`/sources` - Get a list of event sources that provide information about natural events.


## 3. List of features 

### Feature: Display Astronomy Picture of the Day (APOD)

**Description:** Users can view NASA's Astronomy of the Day (APOD) along with relevant information, including a picture, a brief explanation, and the date of the picture.

**Model (data class):** `AstronomyPicture`

**REST API endpoint:** `/apod`

**Pages:** `Display_Astronomy_Picture_of_the_Day_page`


### Feature: Create Daily Earth Photos Gallery

**Description:** Users can select different rovers and dates to explore captivating Martian photos, including those captured by NASA's Curiosity, Spirit, Opportunity, and Perseverance rovers.

**Model (data class):** `DailyEarthView`

**REST API endpoint:** `/photos`

**Pages:** `Daily_Earth_gallery_page`


### Feature: Search Astronomy Pictures

**Description:** Users can explore captivating photos of both Earth. They can select different dates to view daily Earth photos taken by NASA's Earth Polychromatic Imaging Camera (EPIC).

**Model (data class):** `AstronomyPicture`

**REST API endpoint:** `/apod`

**Pages:** `Search_Astronomy_Picture_of_the_Day_page`


### Feature: View Natural Event

**Description:** Users can experience the oddity and beauty of Earth through the View Natural Event feature. 

**Model (data class):** `NaturalEvent`

**REST API endpoint:** `/natural_events`

**Pages:** `View_Natural_Event_page`


## 4. References to any external resources you will use

I will use datetime module from the python library.

## 5. Code highlights

### Safely Accessing Nested Data

One of the more challenging aspects of working with the NASA API was handling the deeply nested JSON structures safely. Here's how I ensured my application could handle missing data gracefully:

In this project, I tackled the intricate task of extracting and displaying nested JSON data from NASA's APIs. The following snippets showcase my approach to accessing this nested information safely and robustly:

```python
# Handling nested 'geometries' data to retrieve dates
geometries = event.get('geometries', [{}])
if geometries:
    st.write('Date:', geometries[0].get('date', 'No Date'))

# Accessing 'categories' information to determine the event type
categories = event.get('categories', [{}])
if categories:
    st.write('Type:', categories[0].get('title', 'No Type'))
```

## 6. Next steps

With more time allotted to this project, I would focus on the following feasible improvements:

- **Enhance Caching**: Implement advanced caching mechanisms to store API responses and reduce load times, ensuring a smooth user experience even with high traffic.
  
- **User Interface Polish**: Improve the user interface with interactive elements like sliders for date selection, enhancing the visual appeal and usability of the app.

- **Expand Content**: Integrate additional NASA APIs to offer a wider range of data, such as real-time satellite imagery or Mars rover photos.

- **User Feedback Loop**: Establish a system for user feedback to guide future updates, ensuring the app evolves in line with user needs and interests.

## 7. Reflection

Throughout this project, I've deepened my understanding of working with external APIs and enhanced my skills in handling JSON data. The most challenging aspect was ensuring the app gracefully handles API rate limits and data variability. Conversely, the most rewarding part was seeing the application come to life, displaying rich content from NASA and providing a gateway to the wonders of our universe. If I were to approach this project again, I would allocate more time for testing edge cases and focus on optimizing the app's performance to better handle user interactions and data processing.
