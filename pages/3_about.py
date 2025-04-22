import streamlit as st
from PIL import Image

st.set_page_config(page_title="About", page_icon="👤", layout="centered")
lake_og = Image.open("assets/lake.png")
lake = lake_og.resize((1920,1280))

st.title("About me")


st.header("Let's Connect!", divider=True)

# Step 4: Footer Section (Optional)
st.markdown("""
    Feel free to reach out to me via:
    - [LinkedIn](https://www.linkedin.com/in/sidhaus/)
    - [Email](mailto:sid1dabholkar@gmail.com)
""")

st.header("Some of my inspirations!", divider=True)

st.markdown("""
    - Bittersweet - book by Susan Cain
    - The Perks of Being a Wallflower - book by Stephen Chbosky
    - Alan Wake / Alan Wake 2 - games by Remedy Entertainment
    - Inception - film directed by Christopher Nolan
    - The Batman - film directed by Matt Reeves
    - The Shining - film directed by Stanley Kubrick
    - Legion - TV show whose showrunner was Noah Hawley
""")


# Optional: Display a background image (e.g., logo or header)
st.image(lake)
