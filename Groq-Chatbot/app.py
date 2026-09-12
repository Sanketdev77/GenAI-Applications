import streamlit as st

from llm import get_chat_response

st.set_page_config(page_title="Finance chatbot",
                   page_icon=":money_with_wings:")

st.title("Finance chatbot app")

## session_state: to preserve info between the reruns
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# create sidebar for chat history
st.sidebar.header("Chat History")

## extract only user questions from the conversation history. 
## becuase chat_history contains both:
## a. role = user, b. role = assistant

user_queries = [
    msg["content"]
    for msg in st.session_state.chat_history
    if msg["role"] == "user"
]

## Display previous questions in sidebar
if user_queries:
    for i, query in enumerate(user_queries, 1):
        st.sidebar.write(
            f"{i}.{query}"
        )
else:
    st.sidebar.write("No chat history available")

## Create user input box
user_input = st.text_input("Ask me anything about finances")

## process the question when the user clicks Send
if st.button("Send"):
    ## we will validate the input. strip() will remove leading and trailing white spaces
    if user_input.strip() == "":
        st.warning("Please enter a valid query.")
    else:
        response = get_chat_response(
            user_input,
            st.session_state.chat_history
        )

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    st.session_state.chat_history.append(
        {
            "role":"assistant",
            "content": response
        }
    )

## Display the conversation

st.subheader("Conversation")

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.write(
            f"**User:** {msg['content']}"
        )
    else:
        st.write(
            f"**Chatbot:** {msg['content']}"
        )
