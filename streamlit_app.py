import streamlit as st
from contact_help import contact_help
from classify_depression import classify_depression
from user_manual import user_manual

# Set page config
st.set_page_config(
    page_title="DepresCare",
    page_icon="🧠",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Main Page", "Classify Depression", "Contact Help", "User Manual"])

def main_page():
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

    st.markdown("---")
    st.markdown('<p style="text-align:center;">Click the button below to check your Depression based on PHQ-9</p>', unsafe_allow_html=True)
    
    # Button to navigate to classification page
    if st.button("CLICK"):
        st.session_state.page = "Classify Depression"

if page == "Main Page":
    main_page()
elif page == "Classify Depression":
    classify_depression()
elif page == "Contact Help":
    contact_help()
elif page == "User Manual":
    user_manual()
