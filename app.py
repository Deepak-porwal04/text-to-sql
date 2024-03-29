from src.gemini_wrapper import get_response_as_sql_query, get_query_response_as_text, configure_gemini
from utils.prompts import system_prompt
import streamlit as st

# Initialize Gemini model with API key
configure_gemini()

# Set up Streamlit page configuration
st.set_page_config(page_title="Text to SQL query Generator")
st.header("Database Retriever")
# Input box for user's question
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    with st.spinner("Loading SQL code..."):
        # Generate SQL code using the Gemini model
        response_sql = get_response_as_sql_query(question, system_prompt)

    st.subheader("SQL Code:")
    st.code(response_sql)

    with st.spinner("Loading data..."):
        # Retrieve database response based on the generated SQL code
        data = get_query_response_as_text(response_sql)

     # Display the retrieved database response
    st.subheader("The response is: ")
    for row in data:
        st.write(row)