import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgC'

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
    st.title("AI Assistant with Conversational History")

    # Initialize session state for conversation history
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = ""

    query = st.text_input("Enter your question:")

    if query:
        with st.spinner("Getting AI response..."):
            final_prompt = st.session_state.conversation_history + "You: " + query + "\n"
            ai_response = ask_gpt(final_prompt)
            st.session_state.conversation_history += "You: " + query + "\n" + "AI: " + ai_response + "\n"
            st.write(f"AI response: {ai_response}")

    # Display the conversation history
    st.subheader("Conversation History")
    st.text(st.session_state.conversation_history)

if __name__ == "__main__":
    main()
