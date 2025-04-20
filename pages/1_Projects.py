import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="Projects", page_icon="📊", layout="wide")

img1 = Image.open("assets/demo_dashboard_scrn.png")
demo_img = ImageOps.expand(img1, border=(5, 5, 5, 5), fill="black")

st.title("📊 My Projects")
st.write("Here's a list of the dashboards, tools, and data stories I’ve created.")

st.header("Current Projects")
# — Demo Dashboard Card — 
st.subheader("Project 1: Demo Dashboard")
st.write("""
A simple csv upload and Altair line chart demo. Upload your own csv file and pick X/Y columns to see an interactive plot.
""")
#st.markdown("[Go to Demo Dashboard](demo_dashboard)", unsafe_allow_html=True)
st.page_link("pages/demo_dashboard.py", label="Go to Demo Dashboard")
#st.markdown("[Go to Demo Dashboard](demo_dashboard)")
st.image(demo_img, caption="Demo showing Altair line chart demo")

# Link to the multipage dashboard
st.markdown("---")

# — Future Project Cards —
#  copy/paste the block below for each new project:
#
# st.subheader("Project Title")
# img = Image.open("assets/your_screenshot.png")
# st.image(img, caption="Preview", use_container_width=True)
# st.write("One‑liner about what it does.")
# st.markdown("[▶️ Open Project](your_page_filename)")


# Step 3: Displaying Future Projects
st.header("Future Projects")

# Future Project 1
st.subheader("Project: Costing Dashboard")
st.write("""
    A dashboard for assessing various cost models. Logarithmic, etc.
""")
#img = Image.open("supply_chain_dashboard.png")  # Make sure the image is in the right folder
#st.image(img, caption="Supply Chain Dashboard", use_container_width=True)

# Future Project 2
st.subheader("Project: Gaming Mood Dashboard")
st.write("""
    Track mood vs. game usage using open or simulated data.
""")


