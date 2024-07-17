import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import Classify_Depression
import Contact
import User_Manual

# Custom CSS to style buttons and sections
st.markdown(
    """
    <style>
    .section-container {
        display: flex;
        align-items: flex-start; /* Adjusted alignment */
        background-color: #f5deb3; /* Light brown */
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    }
    .button {
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-right: 20px;
        min-width: 150px; /* Fixed width for buttons */
        text-align: center;
        font-size: 16px;
        font-weight: bold;
    }
    .button-textbox {
        background-color: #333333; /* Light black */
    }
    .button-classify {
        background-color: black;
        color: white; /* White text */
    }
    .button-classify:hover {
        background-color: #1a1a1a; /* Darkened black on hover */
        color: red;
    }
    .button-next,
    .button-return,
    .button-click {
        background-color: blue; /* Blue */
    }
    .section-content {
        flex: 1;
        margin-left: 20px;
        font-size: 16px;
        color: black; /* Text color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Define the options for the menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",
            options=["Home", "Classify Depression", "Contact", "User Manual"],
            icons=["house", "search", "envelope", "question-circle"],
            menu_icon="cast",
            default_index=0,
        )

    # Navigation logic based on selected option
    if selected == "Home":
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

    elif selected == "Classify Depression":
        Classify_Depression.main()

    elif selected == "Contact":
        Contact.main()

    elif selected == "User Manual":
        User_Manual.main()

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

    # Define the link to Classify Depression page
    classify_depression_link = "/Classify_Depression"

    # Display the button with a link to Classify Depression page
    if st.button("CLICK"):
        st.markdown(f'<a href="{classify_depression_link}">Go to Classify Depression Page</a>', unsafe_allow_html=True)

# Run the main function to display the user guide
if __name__ == "__main__":
    main()
