import requests
import streamlit as st

api_key = "Jf22lOK7OChcnUzHTc5objHfVvbnNent0TFclfa8"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

image_filepath = "img.png"
response = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
