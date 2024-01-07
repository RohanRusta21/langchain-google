from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

st.title("Rohan's Own ChatGPT")

# Create a sidebar for user input
with st.sidebar:
    google_api_key = st.text_input("Gemini API Key", key="langchain_search_api_key_gemini", type="password")

# Create a text input for user query
user_query = st.text_input("Enter your query:")

# Check if the user has entered a query before invoking the model
if user_query:
    # Initialize ChatGoogleGenerativeAI with the provided Gemini API key
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=google_api_key)

    # Invoke the model with the user's query
    result = llm.invoke(user_query)

    # Display the result below the input field
    st.write("Answer:", result.content)
