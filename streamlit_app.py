import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'

# Function to interact with OpenAI GPT
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

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
