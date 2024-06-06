import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgC'

# Function to interact with OpenAI GPT
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

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
