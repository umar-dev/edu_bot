import streamlit as st
import openai
import os


# Retrieve OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY", "")

# ChatGPT function with an education-related prompt
def ask_chatgpt_education(question):
    prompt = f"Education: {question}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

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
