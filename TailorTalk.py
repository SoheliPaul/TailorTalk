import os
from dotenv import load_dotenv
import streamlit as st
from typing import Generator
from groq import Groq

load_dotenv()
st.set_page_config(page_icon="💬", layout="wide", page_title="TailorTalk")

st.subheader("TailorTalk", anchor=False)
st.write("Hello! I'm your friendly chatbot. I can help answer your questions, provide information, and have a conversation. I'm also super fast! Let's start our conversation!")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize chat history and selected model
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = ""  # Leave blank, to be filled by user

if "last_response" not in st.session_state:
    st.session_state.last_response = ""  # Store the last response for adjustment

# Define model details
models = {
    "gemma-7b-it": {"name": "Gemma-7b", "tokens": 8192, "developer": "Google"},
    "llama3-70b-8192": {"name": "LLaMA3 70b", "tokens": 8192, "developer": "Meta"},
    "llama3-8b-8192": {"name": "LLaMA3 8b", "tokens": 8192, "developer": "Meta"},
    "mixtral-8x7b-32768": {"name": "Mixtral 8x7b", "tokens": 32768, "developer": "Mistral"},
}

with st.sidebar:
    st.title("Chat configuration")

    model_option = st.selectbox(
        "Choose a model you want to chat with:",
        options=list(models.keys()),
        format_func=lambda x: models[x]["name"],
        index=2  # Default to llama
    )

    if st.session_state.selected_model != model_option:
        st.session_state.messages = []
        st.session_state.selected_model = model_option

    # Customizable system prompt
    st.session_state.system_prompt = st.text_area("System Prompt", value=st.session_state.system_prompt)

    # Response length control by number of lines
    response_line_limit = st.slider(
        "Response Length (lines):",
        min_value=1,
        max_value=20,  # Adjust as needed
        value=5,  # Default number of lines
        step=1,
        help="Set the maximum number of lines in the response."
    )

# If the user has entered a system prompt, add it to the chat history
if st.session_state.system_prompt and not any(m["role"] == "system" for m in st.session_state.messages):
    st.session_state.messages.insert(0, {"role": "system", "content": st.session_state.system_prompt})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = '🤖' if message["role"] == "assistant" else '👨‍💻'
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

def generate_chat_responses(chat_completion) -> Generator[str, None, None]:
    """Yield chat response content from the Groq API response."""
    for chunk in chat_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

# Button to generate response
if prompt := st.chat_input("Enter your prompt here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Fetch response from Groq API
    try:
        chat_completion = client.chat.completions.create(
            model=model_option,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            max_tokens=2048,  # Set high enough to get the needed lines
            stream=True
        )

        # Use the generator function with st.write_stream
        with st.chat_message("assistant"):
            chat_responses_generator = generate_chat_responses(chat_completion)
            full_response = "".join(list(chat_responses_generator))

            # Store the full response for later adjustments
            st.session_state.last_response = full_response

            # Limit response to the number of lines specified in the slider
            response_lines = full_response.splitlines()
            limited_response = "\n".join(response_lines[:response_line_limit])
            st.markdown(limited_response)
    except Exception as e:
        st.error(f"Error occurred: {e}")

    # Append the limited response to session_state.messages
    st.session_state.messages.append({"role": "assistant", "content": limited_response})

# Display adjusted response based on slider
if st.session_state.last_response:
    # Re-render the response based on the current slider value
    response_lines = st.session_state.last_response.splitlines()
    limited_response = "\n".join(response_lines[:response_line_limit])
    st.markdown(limited_response)