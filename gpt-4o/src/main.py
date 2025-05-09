import os
import json
import streamlit as st
from openai import OpenAI

# Load API key from config.json file
working_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(working_dir, "config.json")
with open(config_path) as f:
    config_data = json.load(f)

# Use GITHUB_TOKEN from config.json; adjust the key name if needed.
GITHUB_TOKEN = config_data["GITHUB_TOKEN"]

# Initialize OpenAI client with GitHub model integration
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=GITHUB_TOKEN,
)

# Configure Streamlit page
st.set_page_config(
    page_title="GPT-4o Chat",
    page_icon="💬",
    layout="centered"
)

# Initialize chat history
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
    # Display and record user's message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    try:
        # Build messages with a system prompt and conversation history
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.chat_history
        ]

        # Get response from GPT-4o via GitHub endpoint
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=messages,
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        assistant_response = response.choices[0].message.content

        # Record and display assistant's response
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):
            st.markdown(assistant_response)

    except Exception as e:
        st.error(f"An error occurred: {e}")
