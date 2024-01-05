import streamlit as st
from PIL import Image

# Define the URL of the chatbot
chatbot_url = "https://chat.dante-ai.com/embed?kb_id=d7780370-85f7-47b6-a131-fa8028143fbb&token=be9f499a-3c44-41bb-b719-cfdb20592f7c&modeltype=gpt-4&logo=dHJ1ZQ%3D%3D&mode=false"

# Define the height of the iframe
iframe_height = 500

# Define the logo image
logo_url = "leungloyung8.jpg"
logo_width = 120
logo_height = 40

# Define the Streamlit app
def app():
    # Set the app title
    st.set_page_config(page_title="Chatbot App", page_icon=":robot_face:")

    # Load the logo image and resize it to fit the specified dimensions
    logo = Image.open(logo_url)
    logo_aspect_ratio = logo.width / logo.height
    logo = logo.resize((int(logo_height * logo_aspect_ratio), logo_height))

    # Add the logo image
    st.image(logo, width=logo_width)

    # Add a header
    #st.header("Welcome to the Opexil AI!")

    # Define the iframe code as a string
    iframe_code = f'<iframe src="{chatbot_url}" width="125%" height="{iframe_height}" frameborder="0"></iframe>'

    # Add the iframe to the app using markdown
    st.markdown(iframe_code, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
