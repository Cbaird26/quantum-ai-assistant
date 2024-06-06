import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'

# Function to interact with OpenAI GPT
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Simple OpenAI Integration with Streamlit")

    prompt = "Here is our conversation history:\nMe: Hello! How can I help you today?\nYou: I'm looking for information on AI assistants.\nMe: Great! I can help you with that. What specifically would you like to know?\n"
    prompt += "Now, continue the conversation:\nYou:"
    
    query = st.text_input("Enter your question:", "What can AI assistants do?")

    if query:
        with st.spinner("Getting AI response..."):
            final_prompt = prompt + query
            ai_response = ask_gpt(final_prompt)
            st.write(f"AI response: {ai_response}")

if __name__ == "__main__":
    main()
