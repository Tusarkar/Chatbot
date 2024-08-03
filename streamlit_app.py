import streamlit as st
import joblib
from auth import authenticate

def show_login():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(email, password):
            st.session_state["authenticated"] = True
            st.session_state["email"] = email
            st.session_state["page"] = "main"  # Set the page to "main" to trigger redirection
        else:
            st.error("Invalid credentials")

def show_main_app():
    st.title(f"Welcome {st.session_state['email']} to the Streamlit App")
    
    # Load the trained model
    model = joblib.load('qa_retrieval_model.pkl')

    st.title('Question Answering Model')

    # User input
    question = st.text_input('Enter your question:')
    if question:
        # Predict
        answer = model.predict([question])[0]
        st.write('**Answer:**', answer)

# Initialize session state variables
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "login"  # Default page is login

# Navigation based on the page state
if st.session_state["page"] == "main":
    show_main_app()
else:
    show_login()

