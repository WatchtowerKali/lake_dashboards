import streamlit as st
from PIL import Image

st.set_page_config(page_title="About", page_icon="👤", layout="centered")
lake_og = Image.open("assets/lake.png")
lake = lake_og.resize((1920,1280))

st.title("About me")

# Optional: Display a background image (e.g., logo or header)
st.image(lake)


# Step 4: Footer Section (Optional)
st.markdown("""
    #### Let's Connect!
    Feel free to reach out to me via:
    - [LinkedIn](https://www.linkedin.com/in/sidhaus/)
    - [Email](mailto:sid1dabholkar@gmail.com)
""")

