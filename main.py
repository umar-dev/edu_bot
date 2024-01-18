import streamlit as st
import openai
import os


# Retrieve OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

# ChatGPT function with an education-related prompt
def ask_chatgpt_education(conversation):
    
    response =  openai.chat.completions.create(
    model="gpt-4",
    messages= conversation,
    n=1    
    )
    return response.choices[0].message.content

# Streamlit UI
def main():
    st.title("Educational ChatGPT Bot")

    # Initialize conversation with a system message
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # User input
    user_input = st.text_area("Chat with the assistant:", "")

    # Add user message to conversation when the user submits
    if st.button("Send"):
        if user_input:
            conversation.append({"role": "user", "content": user_input})

            # Call the OpenAI function to get the answer
            answer = ask_chatgpt_education(conversation)

            # Add assistant's reply to conversation
            conversation.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()
