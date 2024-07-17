import streamlit as st

# Set the page configuration
st.set_page_config(page_title="DepresCare")

# Function to display the home page
def show_home_page():
    st.markdown('<h1 style="color: orange;">Welcome to DepresCare</h1>', unsafe_allow_html=True)
    st.write("The purpose of DepresCare web application is to help users detect symptoms of depression found in text. "
             "DepresCare can assist users in identifying the type of depression by recognizing their depressive symptoms. "
             "Three symptoms are used to detect depression from PHQ-9, which are:")
    st.markdown("1. Trouble falling or staying asleep, or sleeping too much?")
    st.markdown("2. Feeling tired or having little energy?")
    st.markdown("3. Moving or speaking so slowly that other people could have noticed?")
    
    st.markdown('<h2 style="color: orange;">What is Depression?</h2>', unsafe_allow_html=True)
    st.write("Depression is a mental health disorder characterized by persistent feelings of sadness, loss of interest or pleasure in activities that were once enjoyable, and a range of physical and emotional symptoms. These symptoms can vary in intensity and duration, but they often interfere with a person's ability to function normally in daily life.")
    
    st.markdown('<p style="font-weight:bold; color:orange;">Symptoms are used to detect depression based on PHQ-9 are as below: </p>', unsafe_allow_html=True)

    # Create a button with styling to navigate to Classify_Depression page
    if st.button("CLICK", key="click_button", help="Click to classify depression"):
        # Set the session state to navigate to the classification page
        st.session_state['page'] = 'Classify_Depression'
        st.experimental_rerun()

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

# Function to display the classification page
def show_classification_page():
    import Classify_Depression
    Classify_Depression.main()

# Initialize the session state if not already done
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'  # Default page

# Routing logic
if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'Classify_Depression':
    show_classification_page()
