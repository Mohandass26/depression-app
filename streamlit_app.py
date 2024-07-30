import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import Classify_Depression
import Contact
import User_Manual

# Function to switch between pages using URL parameters
def switch_page(page_name: str):
    st.experimental_set_query_params(page=page_name)
    st.session_state.page = page_name  # Ensure the session state is updated

# Initialize session state based on query parameters
query_params = st.experimental_get_query_params()
if 'page' not in st.session_state:
    st.session_state.page = query_params.get('page', ["Main"])[0]

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Main", "Classify Depression", "Contact", "User Manual"],
        icons=["house", "search", "envelope", "book"],
        menu_icon="cast",
        default_index=0,
    )

    # Update session state and query parameters based on sidebar selection
    if selected:
        switch_page(selected)

# Function to set the background image
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Main content based on selected option
if st.session_state.page == "Main":
    set_background_image("https://media.istockphoto.com/id/450153013/vector/editable-vector-of-man-on-chair-with-head-in-hand.jpg?s=612x612&w=0&k=20&c=AxIo6RSthT11grRN1Ra5zjvm6yvn_A92MJVEUPPmUNI=")

    st.markdown('<h1 style="color: orange;">DepresCare</h1>', unsafe_allow_html=True)
    st.write("The purpose of DepresCare web application is to help users detect symptoms of depression found in text. "
             "DepresCare can assist users in identifying the type of depression by recognizing their depressive symptoms. "
             "Three symptoms are used to detect depression from PHQ-9, which are:")

    st.markdown("1. Trouble falling or staying asleep, or sleeping too much?")
    st.markdown("2. Feeling tired or having little energy?")
    st.markdown("3. Moving or speaking so slowly that other people could have noticed?")

    st.markdown('<h2 style="color: orange;">What is Depression?</h2>', unsafe_allow_html=True)

    st.write("Depression is a mental health disorder characterized by persistent feelings of sadness, loss of interest or pleasure in activities that were once enjoyable, and a range of physical and emotional symptoms. These symptoms can vary in intensity and duration, but they often interfere with a person's ability to function normally in daily life.")

    st.markdown("######")

    st.markdown('<p style="font-weight:bold; color:orange;">Symptoms used to detect depression based on PHQ-9:</p>', unsafe_allow_html=True)

    # Load Depression Lexicon
    @st.cache_data
    def load_lexicon():
        return pd.read_csv('Depression_lexicon.csv')

    lexicon = load_lexicon()
    st.write(lexicon)

    st.markdown("---")
    st.markdown('<p style="text-align:center;">Click on the navigation to classify your depression based on PHQ-9</p>', unsafe_allow_html=True)

    if st.button("CLICK"):
        st.session_state.page = "Classify Depression"  # Set the session state to "Classify Depression"
        st.experimental_rerun()  # Rerun the script to navigate to the new page

elif st.session_state.page == "Classify Depression":
    Classify_Depression.main()

elif st.session_state.page == "Contact":
    Contact.main()

elif st.session_state.page == "User Manual":
    User_Manual.main()
