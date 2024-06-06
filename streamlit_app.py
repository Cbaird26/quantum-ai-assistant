import streamlit as st
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Options
from qiskit import QuantumCircuit, transpile
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'

# Load IBM Quantum account and set up service
service = QiskitRuntimeService(
    token='efaee3112cb68eb568bde505587ca5c445cb28d0469c0704bd13d947fa7db08bc',
    channel='ibm_quantum',
)

# Function to run a quantum circuit
def run_quantum_circuit(circuit, backend_name):
    backend = service.backend(backend_name)
    transpiled_circuit = transpile(circuit, backend=backend)
    job = backend.run(transpiled_circuit)
    result = job.result()
    return result

# Function to interact with OpenAI GPT-4 using the correct API method
def ask_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def main():
    st.title("Quantum AI Assistant")
    
    query = st.text_input("Enter your question:")
    
    if query:
        ai_response = ask_gpt4(query)
        st.write(ai_response)

if __name__ == "__main__":
    main()
