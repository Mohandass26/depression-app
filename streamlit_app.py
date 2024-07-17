import streamlit as st
import pandas as pd
import string
import re

# Set page config
st.set_page_config(
    page_title="DepresCare"
)

# Load Depression Lexicon
@st.cache_data
def load_lexicon():
    return pd.read_csv('Depression_lexicon.csv')

# Load the trained model and vectorizer
@st.cache_data
def load_model():
    model = load('logistic_model.pkl')
    vectorizer = load('tfidf_vectorizer.pkl')
    return model, vectorizer

# Define function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Define function to clean text
def clean_text(text):
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()
        # Remove all punctuation except apostrophe
        text = ''.join([char for char in text if char not in string.punctuation or char == "'"])
        # Remove numbers
        text = re.sub(r'\d+', '', text)
    return text

# Define function to detect depression signals
def detect_depression(text, signals):
    if text is not None and isinstance(text, str):  # Ensure text is not None and is a string
        text = preprocess_text(text)  # Preprocess the text
        matched_signals = [signal for signal in signals if isinstance(signal, str) and signal.lower() in text]
        return matched_signals if matched_signals else []
    return []

# Main page content
def main_page():
    st.markdown('<h1 style="color: orange;">DepresCare</h1>', unsafe_allow_html=True)
    st.write("The purpose of DepresCare web application is to help users detect symptoms of depression found in text. "
             "DepresCare can assist users in identifying the type of depression by recognizing their depressive symptoms. "
             "Three symptoms are used to detect depression from PHQ-9, which are:")
    st.markdown("1. Trouble falling or staying asleep, or sleeping too much?")
    st.markdown("2. Feeling tired or having little energy?")
    st.markdown("3. Moving or speaking so slowly that other people could have noticed.?")
    st.markdown('<h2 style="color: orange;">What is Depression?</h2>', unsafe_allow_html=True)
    st.write("Depression is a mental health disorder characterized by persistent feelings of sadness, loss of interest or pleasure in activities that were once enjoyable, and a range of physical and emotional symptoms. These symptoms can vary in intensity and duration, but they often interfere with a person's ability to function normally in daily life.")
    st.markdown("######")
    st.markdown('<p style="font-weight:bold; color:orange;">Symptoms are used to detect depression based on PHQ-9 are as below: </p>', unsafe_allow_html=True)

    # Load Depression Lexicon
    lexicon = load_lexicon()

    # Display lexicon data
    st.write(lexicon)

    st.markdown("---")
    st.markdown('<p style="text-align:center;">Click the button below to check your Depression based on PHQ-9</p>', unsafe_allow_html=True)
    
    # Button to navigate to classification page
    if st.button("CLICK"):
        st.session_state.page = "Classify_Depression"

# Classification page content
def classify_depression():
    st.markdown('<h1 style="color: orange;">Welcome to DepresCare</h1>', unsafe_allow_html=True)
    st.subheader("Text classifier for users based on emotions and feelings during that situations for detect depression")

    # Load Depression Lexicon
    lexicon = load_lexicon()

    # Extract PHQ signals
    try:
        phq3_col = 'Trouble falling or staying asleep, or sleeping too much?'
        phq4_col = 'Feeling tired or having little energy?'
        phq8_col = 'Moving or speaking so slowly that other people could have noticed.?'

        depression_signals_phq3 = lexicon[phq3_col].dropna().tolist()
        depression_signals_phq4 = lexicon[phq4_col].dropna().tolist()
        depression_signals_phq8 = lexicon[phq8_col].dropna().tolist()
    except KeyError as e:
        st.error(f"KeyError: {e}. Please check the column names in the CSV file.")
        depression_signals_phq3 = []
        depression_signals_phq4 = []
        depression_signals_phq8 = []

    # Text classification form
    if 'text' not in st.session_state:
        st.session_state.text = ""

    st.session_state.text = st.text_area("Enter your text here", st.session_state.text)

    if st.button("CLASSIFY"):
        if st.session_state.text.strip() == "":
            st.error("No text entered. Please enter some text to classify.")
        else:
            preprocessed_text = clean_text(st.session_state.text)
            phq3_signals = detect_depression(preprocessed_text, depression_signals_phq3)
            phq4_signals = detect_depression(preprocessed_text, depression_signals_phq4)
            phq8_signals = detect_depression(preprocessed_text, depression_signals_phq8)

            detected_signals = {
                'Trouble falling or staying asleep (PHQ-3)': phq3_signals,
                'Feeling tired (PHQ-4)': phq4_signals,
                'Moving or speaking so slowly (PHQ-8)': phq8_signals
            }

            # Display results
            st.success(f"Preprocessed text: {preprocessed_text}")
            if any(detected_signals.values()):
                st.write("Based on your text, here are the detected depression symptoms:")
                for phq, signals in detected_signals.items():
                    st.write(f"Detected Signals for {phq} : {signals}")
                st.error("Based on the result, you MAY HAVE DEPRESSION. Please click NEXT for further information to seek for professional help .")
            else:
                st.write(f"No depression signals detected in the text: {st.session_state.text}.")
                st.error("Based on the depression signals of Trouble falling or staying asleep (PHQ-3), Feeling tired (PHQ-4) and Moving or speaking so slowly (PHQ-8) symptoms.")

            # Navigation buttons
            col1, col2 = st.columns([1, 1])
            with col1:
                st.button("RETURN")
            with col2:
                if any(detected_signals.values()):
                    st.button("NEXT")

# Main app logic
if 'page' not in st.session_state:
    st.session_state.page = "Main"

if st.session_state.page == "Main":
    main_page()
elif st.session_state.page == "Classify_Depression":
    classify_depression()
