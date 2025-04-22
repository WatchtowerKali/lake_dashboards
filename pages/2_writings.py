import streamlit as st
from PIL import Image

st.set_page_config(page_title="writings", page_icon="👤", layout="centered")
lake_og = Image.open("assets/lake.png")
lake = lake_og.resize((1920,1280))

st.title("Writings")

st.header("future thoughts")

st.write("""
    - [Metaverse thoughts - Pitfalls](https://medium.com/quarter-life-crisis/alone-but-not-lonely-metaverses-pitfalls-and-opportunities-part-1-of-2-c1ee32ccc1a6)
    - [Metaverse thoughts - Opportunities](https://medium.com/@sid_haus/alone-but-not-lonely-metaverses-pitfalls-and-opportunities-part-2-of-2-3a44fdc2b850)
""")

st.header("mental health")

st.write("""
    - [my experience with illness anxiety + fear of death](https://medium.com/many-melancholic-and-merry-musings/suppose-i-reconcile-my-fear-of-death-1077d4cd2f11)
""")

st.header("short stories - horror / scifi")

st.write("""
    - [waking in the silence](https://medium.com/@sid_haus/waking-in-the-silence-chapter-1-e03169293536)
""")

# Optional: Display a background image (e.g., logo or header)
st.image(lake)

