import streamlit as st
import os
from PIL import Image
# Make sure you import the correct library/module for Google Generative AI
import google.generativeai as genai
def ver():
    # Set your Google API key here
    API_KEY = "AIzaSyB6gfvX21wsMuWfl9696C1Hh38zSo446b0"

    # Configure Google API
    os.environ["GOOGLE_API_KEY"] = API_KEY
    genai.configure(api_key=API_KEY)

    # Function to load OpenAI model and get responses
    def get_gemini_response( image, input_prompt):
        model = genai.GenerativeModel('gemini-pro-vision')
        
        response = model.generate_content([ image, input_prompt1])
        

    

    # Input prompt
    name = st.text_input("Username")
    password = st.text_input("Password", key="password")
    password1 = st.text_input("Confirm Password",key="pass")

    # File upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Button to generate response
    submit_button = st.button("VERIFY NOW")
    input_prompt1 = """Hello! Please evaluate the provided image. If it's a doctor's certificate, respond with 'The account will be available soon.' If not, kindly advise 'Please recheck your certificate.' Thank you!.
    """

    # If button is clicked
    if submit_button:
        if image is not None:
            response = get_gemini_response( image, input_prompt1)
            st.subheader("Your condition is")
            st.warning(response)
            print(response)
        else:
            st.warning("Please upload an image before generating response.")
