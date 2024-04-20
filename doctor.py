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
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    if input_text != "":
        response = model.generate_content([input_text, image, input_prompt])
    else:
        response = model.generate_content([image, input_prompt])
    return response.text
def check_credentials(username, password):
    # Replace this with your actual credential checking logic
    return username == "admin" and password == "secret"

def login_section():
    # Login Section
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")
        

    

    # Login Functionality
    if login_button:
        if check_credentials(username, password):
            st.success("Login successful!")
            # Display functionalities or information after successful login
            st.subheader("Welcome, Admin!")
            # Add functionalities accessible only after login (e.g., user management, data visualization)
        else:
            st.error("Invalid username or password!")

# Main content
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
doctor_option = st.sidebar.radio("Select", ("Yes", "No","Register"))

# If user is a doctor, display the login section
if doctor_option == "Yes":
    login_section()



if doctor_option == "Register":
    from im import ver
    ver()

# If user is not a doctor or chooses not to login, display the main content
if doctor_option == "No" or ('login_clicked' in st.session_state and st.session_state.login_clicked):
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

    input_prompt = """Please evaluate the provided image. If it pertains to the medical field, kindly share your professional assessment.
      Otherwise, respond with 'This is not within my expertise.' Thank you!"""

    # If button is clicked
    if submit_button:
        if uploaded_file is not None:
            response = get_gemini_response(query, image, input_prompt)
            st.subheader("Your condition is")
            st.warning(response)
        else:
            st.warning("Please upload an image before generating response.")
