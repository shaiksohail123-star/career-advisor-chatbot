import streamlit as st
from chatbot import get_chatbot_response

st.set_page_config(
    page_title="Career Advisor Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Career Advisor Chatbot")

st.write("Ask career-related questions.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your question...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_chatbot_response(user_input)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )