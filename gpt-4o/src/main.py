import os
import json

import streamlit as st
from openai import OpenAI

# Load API key from config file
working_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(working_dir, "config.json")
with open(config_path) as f:
    config_data = json.load(f)

OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

# Configure Streamlit page
st.set_page_config(
    page_title="GPT-4o Chat",
    page_icon="💬",
    layout="centered"
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display title
st.title("🤖 GPT-4o - ChatBot")

# Display previous chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user prompt
user_prompt = st.chat_input("Ask GPT-4o...")

if user_prompt:
    # Show user's message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    try:
        # Get response from GPT-4o
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                *st.session_state.chat_history
            ]
        )
        assistant_response = response.choices[0].message.content

        # Store and display assistant response
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error(f"An error occurred: {e}")
