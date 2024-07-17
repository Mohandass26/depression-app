import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Main",
)

# Custom title with color
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

st.markdown('<p style="font-weight:bold; color:orange;">Symptoms are used to detect depression based on PHQ-9 are as below: </p>', unsafe_allow_html=True)

# Load Depression Lexicon
@st.cache_data
def load_lexicon():
    return pd.read_csv('Depression_lexicon.csv')

# Loading the lexicon
lexicon = load_lexicon()

# Displaying lexicon data directly
st.write(lexicon)

st.markdown("---")
st.markdown('<p style="text-align:center;">Click the button below to check your Depression based on PHQ-9</p>', unsafe_allow_html=True)

# Create a button with styling
if st.button("CLICK", key="click_button", help="Click to classify depression"):
    # Redirect logic goes here
    # Set a session state or perform some action to handle navigation
    st.session_state['page'] = 'Classify_Depression.py'
   
# CSS for button styling
st.markdown("""
    <style>
        .stButton button {
            background-color: blue;
            color: white;
            padding: 10px 24px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: lightblue;
        }
    </style>
""", unsafe_allow_html=True)
