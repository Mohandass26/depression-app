import streamlit as st

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
        background-color: black;
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

def main():
    # Main title for the user guide
    st.markdown('<h1 style="color: orange;">DepresCare User Guide</h1>', unsafe_allow_html=True)

    # Function to create a styled section with a button and description
    def create_section(button_text, description, button_color_class):
        st.markdown(
            f"""
            <div class="section-container">
                <button class="button {button_color_class}">{button_text}</button>
                <div class="section-content">{description}</div>
            </div>
            """, unsafe_allow_html=True
        )

    # Define the content for each section
    sections = [
        ("Text Box", "Users can fill in the text box with any text they want to express their feelings or emotions during that situation.", "button-textbox"),
        ("CLASSIFY", 'Users can click the "CLASSIFY" button to let the machine classify their text based on selected depressive symptoms found in the PHQ-9 instruments.', "button-classify"),
        ("NEXT", 'Users can click the "NEXT" button to seek professional help for further details.', "button-next"),
        ("RETURN", 'Users can click the "RETURN" button to re-enter the text.', "button-return"),
        ("CLICK", 'Users can press the "CLICK" button to visit the next page for Classifying Depression.', "button-click")
    ]

    # Create sections using the defined content
    for button_text, description, button_color_class in sections:
        create_section(button_text, description, button_color_class)

# Run the main function to display the user guide
if __name__ == "__main__":
    main()
