import streamlit as st
from PIL import Image



st.title(':p')
# Open the image file
image = Image.open('Data/lol.png')

# Display the image in the Streamlit app
st.image(image, caption='Feeling Generous?', use_container_width =False)