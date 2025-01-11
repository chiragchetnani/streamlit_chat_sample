import streamlit as st
import requests

# Streamlit UI
st.title("Chat with Llama API")

# Input field for user query
query = st.text_input("Enter your query:", "")

# Button to send query
if st.button("Send"):
    if query:
        # Streamlit progress bar
        with st.spinner("Fetching response..."):
            try:
                # Send query to the API
                response = requests.post(
                    "http://34.87.33.156:8000/query-stream",
                    json={"query": query},
                    stream=True
                )

                if response.status_code == 200:
                    st.subheader("Response:")
                    response_text = ""
                    # Stream the response in real-time
                    for chunk in response.iter_content(decode_unicode=True):
                        response_text += chunk
                    # Show the complete response in a single text area
                    st.text_area("", value=response_text, height=300)
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a query.")
