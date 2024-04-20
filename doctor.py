import streamlit as st
from PIL import Image
import google.generativeai as genai

# Set your Google API key here
API_KEY = "AIzaSyCzDrfg3Zm0Lbczv-YhdhkTy_JcENq5d1I"

# Configure Google API
import os
os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=API_KEY)

# Function to load OpenAI model and get responses
def get_gemini_response(input_text, image, input_prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_text != "":
        response = model.generate_content([input_text, image, input_prompt])
    else:
        response = model.generate_content([image, input_prompt])
    return response.text

def app():
    from PIL import Image
    st.set_page_config(page_title="IT'S-MED.Ai")


# Load the image
    image = Image.open('scancerlogo.png')
    image_resized = image.resize((100, 100))
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(image_resized)

    with col2:
        st.title('SCANCER')

        st.sidebar.markdown("## SCANCER")
    st.sidebar.markdown("Are you a doctor?")
    st.sidebar.button("Login", key="login_button", help="Click here to login")


     
    

    # Main content
    st.header('How are you feeling today?')

    # Input prompt
    query = st.text_input("Enter additional information/queries", "Eg: Am I pregnant?")

    # File upload
    uploaded_file = st.file_uploader("Upload your scan", type=['jpg', 'png', 'jpeg', 'gif', 'bmp'])
    image = None
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Scan.", use_column_width=True)

    # Button to generate response
    submit_button = st.button("Tell me about my condition")

    input_prompt = """your task is to review the provided image.If the image related to medical field 
    Please share your professional evaluation ,else the image not related to medical field say this is not my job.
    """

    # If button is clicked
    if submit_button:
        if uploaded_file is not None:
            response = get_gemini_response(query, image, input_prompt)
            st.subheader("Your condition is")
            st.warning(response)
        else:
            st.warning("Please upload an image before generating response.")

# Run the app
app()
