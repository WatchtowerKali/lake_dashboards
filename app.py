import streamlit as st
from PIL import Image

me1 = Image.open("assets/me.jpg")
me = me1.resize((400,400))

lake_og = Image.open("assets/lake.png")
lake = lake_og.resize((1920,1280))

# Step 1: Title Section
st.title("Lake House Portfolio")

# Optional: Display a background image (e.g., logo or header)
st.image(lake, caption="Welcome to My Portfolio")

# Step 2: Introduction Section
st.header("About Me")
st.write("""
    Hello there! I'm Lake, a data enthusiast and aspiring psychologist.
""")
st.image(me, caption="that's me!")
st.write("""
    I’m passionate about using technology and research to improve mental health, with a focus on video games and addiction.
    I’ve worked with PowerBI and am learning Streamlit and Python to build interactive data solutions.
""")

# Step 3: Displaying Projects
st.header("Projects")

# Example Project 1: Dashboard
st.subheader("Project 1: Supply Chain Dashboard")
st.write("""
    A detailed dashboard for tracking supply chain continuity. Includes data visualizations and KPIs for monitoring disruptions and delays.
""")
#img = Image.open("supply_chain_dashboard.png")  # Make sure the image is in the right folder
#st.image(img, caption="Supply Chain Dashboard", use_container_width=True)

# Example Project 2: Interactive Loneliness App
st.subheader("Project 2: Interactive Loneliness Intervention")
st.write("""
    An interactive web app designed to help users reduce feelings of loneliness through CBT-based exercises.
""")

# Step 4: Footer Section (Optional)
st.markdown("""
    #### Let's Connect!
    Feel free to reach out to me via:
    - [LinkedIn](https://www.linkedin.com/siddheshdabholkar)
    - [Email](mailto:sid1dabholkar@gmail.com)
""")

if st.button("Click me!"):
    st.write("You clicked the button!")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name} 👋")

age = st.slider("Choose an age", 0, 100, 25)
st.write(f"Selected age: {age}")

mood = st.selectbox("How are you feeling today?", ["Happy", "Okay", "Tired", "Anxious"])
st.write(f"You selected: {mood}")

if st.checkbox("Show project summary"):
    st.write("Here's a quick summary of the project...")

if st.button("Click for Encouragement"):
    st.toast("High five!", icon="🖐️")
    st.success("Nice work!")
    st.warning("Careful! This model uses assumptions 🚧")
    st.error("Oops! Something went wrong 😬")
    st.success("You’re doing amazing! Keep going 💪✨")