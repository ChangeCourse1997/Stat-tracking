import streamlit as st
from PIL import Image
import os 


st.title('AMK HG CSN')
image = Image.open('Data/Team.jpg')

# Display the image in the Streamlit app
st.image(image, caption='Members', use_container_width =True)

if st.button("Go to Stats page"):
    st.switch_page("pages/1-Stats Tracking.py")

