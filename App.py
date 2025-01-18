import streamlit as st
from PIL import Image
import os 


st.title('AMK HG CSN')
st.write(os.getcwd())
st.write(os.listdir())
image = Image.open('Data/Team.jpg')

# Display the image in the Streamlit app
st.image(image, caption='Members', use_container_width =True)