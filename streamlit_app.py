import streamlit as st
import joblib

# Function to authenticate user
def authenticate(email, password):
    # Replace this with your actual authentication logic
    # Example: check against a hardcoded password
    return email == "user1@example.com" and password == "password1"

# Define the prediction function for test case prediction
def predict_steps(description, model):
    return model.predict([description])[0]

# Load the models
text_classification_model = joblib.load('text_classification_model_testcases_latest.pkl')
qa_model = joblib.load('qa_retrieval_model.pkl')

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Sidebar for navigation
def show_sidebar():
    st.sidebar.title("Navigation")
    if st.session_state["authenticated"]:
        page = st.sidebar.radio("Select Page", ["Test Case Predictor", "Question Answering"])
    else:
        page = st.sidebar.radio("Select Page", ["Login"])

    return page

def show_login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(email, password):
            st.session_state["authenticated"] = True
            st.session_state["email"] = email
        else:
            st.error("Invalid credentials")

def show_test_case_predictor():
    st.title("Test Case Description Predictor")

    description = st.text_area("Enter the test case description:")

    if st.button('Predict'):
        if description:
            predicted_steps = predict_steps(description, text_classification_model)
            st.write(f"Predicted Steps: {predicted_steps}")
        else:
            st.write("Please enter a test case description.")

def show_question_answering():
    st.title(f"Welcome {st.session_state['email']} to the Question Answering Model")

    question = st.text_input('Enter your question:')
    if question:
        answer = qa_model.predict([question])[0]
        st.write('**Answer:**', answer)

# Main app logic
page = show_sidebar()

if page == "Login":
    show_login()
elif page == "Test Case Predictor":
    if st.session_state["authenticated"]:
        show_test_case_predictor()
    else:
        st.write("Please log in to access this page.")
elif page == "Question Answering":
    if st.session_state["authenticated"]:
        show_question_answering()
    else:
        st.write("Please log in to access this page.")
