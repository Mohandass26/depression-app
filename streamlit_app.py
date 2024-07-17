import streamlit as st
import pandas as pd
import string
import re
import joblib

# Set page config
st.set_page_config(
    page_title="DepresCare",
    page_icon="🧠",
)

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

# Function to display Contact Help information
def contact_help():
    st.markdown('<h1 style="color: orange;">Contact Help</h1>', unsafe_allow_html=True)

    st.markdown('<h3 style="color: orange;">Malaysian Mental Health Association (MMHA)</h3>', unsafe_allow_html=True)
    st.write("**Email:** info@mmha.org.my")
    st.write("**Contact:** +60 3-2780 6803")
    st.markdown("""
    For more information and resources, you can visit the [Malaysian Mental Health Association (MMHA) website](https://www.mmha.org.my).
    """)

    st.markdown("---")

    st.markdown('<h3 style="color: orange;">UKM Counselling</h3>', unsafe_allow_html=True)
    st.write("**Address:**")
    st.write("Pusat Hal Ehwal Pelajar (HEP-UKM)")
    st.write("Aras 7, Bangunan PUSANIKA")
    st.write("43600 UKM, Bangi Selangor, MALAYSIA")
    st.write("**Email:** hep@ukm.edu.my")
    st.write("**Contact:** +603-8921 5347")
    st.markdown("""
    For more information and resources, you can visit the [UKM Counseling Unit website](https://www.ukm.my/hepukm/unit-kaunseling-2/).
    """)

    st.markdown("---")

    st.markdown('<h1 style="color: orange;">Need Help?</h1>', unsafe_allow_html=True)
    st.write("""
    If you need help, please do not hesitate to contact the admin. We are here to assist you with any issues or questions you may have.
    """)

    st.markdown("---")

    st.markdown('<h3 style="color: orange;">Contact Admin</h3>', unsafe_allow_html=True)
    st.write("**Admin Name:** Mohandass")
    st.write("**Email:** a189202@siswa.ukm.edu.my")

# Main page content
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

    # Load Depression Lexicon
    lexicon = load_lexicon()

    # Display lexicon data
    st.write(lexicon)

    st.markdown("---")
    st.markdown('<p style="text-align:center;">Click the button below to check your Depression based on PHQ-9</p>', unsafe_allow_html=True)
    
    # Button to navigate to classification page
    if st.button("CLICK"):
        st.session_state.page = "Classify Depression"

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
        phq8_col = 'Moving or speaking so slowly that other people could have noticed?'

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
                    if st.button("NEXT"):
                       st.session_state.page = "Contact Help"

# User Manual content
def user_manual():
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
    }
    .button-textbox {
        background-color: #333333; /* Light black */
    }
    .button-classify {
        background-color: black;
        color: white; /* White text */
    }
    .button-classify:hover {
         background-color:black;
         color: red;
    }
    .button-next {
        background-color: blue; /* Blue */
    }
    .button-return {
        background-color: blue; /* Blue */
    }
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

st.markdown('<h1 style="color: orange;">DepresCare User Guide</h1>', unsafe_allow_html=True)

def create_section(button_text, description, button_color_class):
    st.markdown(
        f"""
        <div class="section-container">
            <button class="button {button_color_class}">{button_text}</button>
            <div class="section-content">{description}</div>
        </div>
        """, unsafe_allow_html=True
    )

# Define each section separately with button_text outside the function call
button_texts = [
    "Text Box",
    "CLASSIFY",
    "NEXT",
    "RETURN",
    "CLICK"
]

descriptions = [
    "Users can fill in the text box with any text they want to express their feelings or emotions during that situation.",
    'Users can click the "CLASSIFY" button to let the machine classify their text based on selected depressive symptoms found in the PHQ-9 instruments.',
    'Users can click the "NEXT" button to seek professional help for further details.',
    'Users can click the "RETURN" button to re-enter the text.',
    'Users can press the "CLICK" button to visit the next page for Classifying Depression.'
]

button_colors = [
    "button-textbox",
    "button-classify",
    "button-next",
    "button-return",
    "button-click"
]

# Mapping button colors to button texts
button_color_map = {
    "Text Box": "button-textbox",
    "CLASSIFY": "button-classify",
    "NEXT": "button-next",
    "RETURN": "button-return",
    "CLICK": "button-click"
}

for i in range(len(button_texts)):
    create_section(button_texts[i], descriptions[i], button_color_map[button_texts[i]])

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Main Page", "Classify Depression", "Contact Help", "User Manual"])

if page == "Main Page":
    main_page()
elif page == "Classify Depression":
    classify_depression()
elif page == "Contact Help":
    contact_help()
elif page == "User Manual":
    user_manual()
