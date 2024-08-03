import streamlit as st
import joblib

# Load the trained model
model = joblib.load('qa_retrieval_model.pkl')

st.title('Question Answering Model')

# User input
question = st.text_input('Enter your question:')
if question:
    # Predict
    answer = model.predict([question])[0]
    st.write('**Answer:**', answer)
