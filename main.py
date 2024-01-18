import streamlit as st
import openai
import os


# Retrieve OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

# ChatGPT function with an education-related prompt
def ask_chatgpt_education(question):
    prompt = f"Education: {question}"
    response =  openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": question,
        },
    ],
  )
 return response.choices[0].message.content

# Streamlit UI
def main():
    st.title("Educational ChatGPT Bot")

    # Input box for user question
    question = st.text_input("Ask a programming-related question:")
    
    if st.button("Get Answer"):
        if question:
            # Call the ChatGPT function to get the answer
            answer = ask_chatgpt_education(question)
            st.subheader("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
