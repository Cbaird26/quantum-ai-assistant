import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgC'

# Function to interact with OpenAI GPT-4
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content'].strip()

# Streamlit app
def main():
    st.title("Simple OpenAI Integration with Streamlit")

    query = st.text_input("Enter your question:")

    if query:
        with st.spinner("Getting AI response..."):
            ai_response = ask_gpt(query)
            st.write(f"AI response: {ai_response}")

if __name__ == "__main__":
    main()
