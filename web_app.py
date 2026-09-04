import time

import streamlit as st
from configure import ChatBot


def response_generator(prompt: str):
    response = st.session_state.bot.chat(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chef Chinonso's Cuisines")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize chatbot once per Streamlit session
if "bot" not in st.session_state:
    st.session_state.bot = ChatBot()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar="👩🏾‍🍳"):
        placeholder = st.empty()

        full_response = st.session_state.bot.chat(prompt)

        displayed_response = ""

        for char in full_response:
            displayed_response += char
            placeholder.markdown(displayed_response)
            time.sleep(0.01)

        response = full_response

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
