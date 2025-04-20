import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")
# Sidebar content
#st.sidebar.title("📂 Navigation")
#st.sidebar.markdown("Use the sidebar to navigate through the site.")
#st.sidebar.page_link("Home.py", label="🏠 Home")
#st.sidebar.page_link("About.py", label="👤 About")
#st.sidebar.page_link("Projects.py", label="📊 Projects")



me1 = Image.open("assets/me.jpg")
me = me1.resize((400,400))

# Step 1: Title Section
st.title("Lake House Portfolio")

# Step 2: Introduction Section
st.header("Hello there!")
st.write("""
    I'm Lake, a data enthusiast and aspiring psychologist.
""")
st.image(me, caption="that's me!")
st.write("""
    I’m passionate about using technology and research to improve mental health, with a focus on video games and addiction.
    I’ve worked with PowerBI and am learning Streamlit and Python to build interactive data solutions.
""")

st.write("""
    This is the home page of my portfolio. Use the sidebar to explore projects, dashboards, and more!
""")

#st.write("""
#    This is the home page of my portfolio. Use the sidebar to explore projects, dashboards, and more!
#         Here's a sample of one of my projects!
#""")