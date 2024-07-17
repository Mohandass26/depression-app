# main.py
import streamlit as st
from streamlit_option_menu import option_menu
import Classify_Depression
import Contact

st.set_page_config(
    page_title="DepresCare",
    page_icon="🏠",
    layout="centered"
)

# Custom title with color
st.markdown('<h1 style="color: orange;">DepresCare</h1>', unsafe_allow_html=True)

# Define the options for the menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Classify Depression", "Contact", "Help"],
        icons=["house", "search", "envelope", "question-circle"],
        menu_icon="cast",
        default_index=0,
    )

# Navigation logic based on selected option
if selected == "Home":
    st.write("The purpose of DepresCare web application is to help users detect symptoms of depression found in text. "
             "DepresCare can assist users in identifying the type of depression by recognizing their depressive symptoms. "
             "Three symptoms are used to detect depression from PHQ-9, which are:")

    st.markdown("1. Trouble falling or staying asleep, or sleeping too much?")
    st.markdown("2. Feeling tired or having little energy?")
    st.markdown("3. Moving or speaking so slowly that other people could have noticed?")

    st.markdown('<h2 style="color: orange;">What is Depression?</h2>', unsafe_allow_html=True)

    st.write("Depression is a mental health disorder characterized by persistent feelings of sadness, loss of interest or pleasure in activities that were once enjoyable, and a range of physical and emotional symptoms. These symptoms can vary in intensity and duration, but they often interfere with a person's ability to function normally in daily life.")

elif selected == "Classify Depression":
    Classify_Depression.main()

elif selected == "Contact":
    Contact.main()

elif selected == "Help":
    st.write("Help page content goes here. Provide relevant help information and resources.")
