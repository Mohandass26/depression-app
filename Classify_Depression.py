import streamlit as st
import pandas as pd
import string
import re
import joblib

# Load Depression Lexicon
@st.cache_data
def load_lexicon():
    return pd.read_csv('Depression_lexicon.csv')

# Load the trained model and vectorizer
@st.cache_data
def load_model():
    model = joblib.load('logistic_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_model()

# Loading the lexicon and combining PHQ signals
lexicon = load_lexicon()

# Extract depression signals for PHQ-3, PHQ-4, and PHQ-8
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

# Define a function for text preprocessing
def preprocess_text(text):
    text = text.lower()  # Convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    return text

# Define a function to check for partial string matching between the text and any depression signal
def detect_depression(text, signals):
    if text is not None and isinstance(text, str):  # Ensure text is not None and is a string
        text = preprocess_text(text)  # Preprocess the text
        matched_signals = [signal for signal in signals if isinstance(signal, str) and signal.lower() in text]
        return matched_signals if matched_signals else []
    return []

# Define a function to clean text
def clean_text(text):
    if isinstance(text, str):
        # Convert to lowercase
        text = text.lower()
        # Remove all punctuation except apostrophe
        text = ''.join([char for char in text if char not in string.punctuation or char == "'"])
        # Remove numbers
        text = re.sub(r'\d+', '', text)
    return text

# Custom title with color
st.markdown('<h1 style="color: orange;">Welcome to DepresCare</h1>', unsafe_allow_html=True)
st.subheader("Text classifier for users based on emotions and feelings during that situations for detect depression")

# Using session state to manage text input
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

        # Transform the text using the loaded vectorizer
        text_vectorized = vectorizer.transform([preprocessed_text])
        
        # Predict using the loaded model
        prediction_proba = model.predict_proba(text_vectorized)[0][1]  # Probability of being "Depressed"
        #st.write(f"Debug: Prediction Probability: {prediction_proba}")  # Debug line to check probability
        
        #prediction = "Depressed" if prediction_proba > 0.005 else "Not Depressed"  # Use 0.5 as threshold for classification

        if any(detected_signals.values()):
            prediction = "Depressed"
            st.success(f"Preprocessed text: {preprocessed_text}")
            st.write("Based on your text, here are the detected depression symptoms:")
            for phq, signals in detected_signals.items():
                st.write(f"Detected Signals for {phq} : {signals}")
            st.error(f"Prediction: {prediction}")
            st.markdown('<p style="font-weight:bold; color:orange;">Based on the result, you MAY HAVE DEPRESSION. Please click NEXT for further information to seek for professional help .</p>', unsafe_allow_html=True)
            st.markdown("---")
            st.write("Please click NEXT for further information or RETURN to classify another text.")
        else:
            prediction = "Not Depressed"
            st.success(f"Preprocessed text: {preprocessed_text}")
            st.write(f"No depression signals detected in the text: {st.session_state.text}.")
            st.write("Based on the depression signals of Trouble falling or staying asleep (PHQ-3), Feeling tired (PHQ-4) and Moving or speaking so slowly (PHQ-8) symptoms.")
            st.success(f"Prediction: {prediction}")
            st.markdown("---")
            st.write("Please click RETURN to classify another text.")

        # Add navigation buttons based on the prediction
        col1, col2 = st.columns([1, 1])

        # Style buttons with unique identifiers
        with col1:
            st.markdown("""
              <a href="/Classify_Depression">
                <button style="background-color: blue; color: white; padding: 10px 24px; border: none; cursor: pointer; font-size: 16px; border-radius: 8px;" onclick="window.location.reload();">
                    RETURN
                </button>
            """, unsafe_allow_html=True)

        if prediction == "Depressed":
            with col2:
                st.markdown("""
                    <a href="/Contact">
                        <button style="background-color: blue; color: white; padding: 10px 24px; border: none; cursor: pointer; font-size: 16px; border-radius: 8px;">
                            NEXT
                        </button>
                    </a>
                """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'><a href='/Help'>Need help?</a></p>", unsafe_allow_html=True)
