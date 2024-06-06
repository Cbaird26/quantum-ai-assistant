import streamlit as st
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Options
from qiskit import QuantumCircuit, transpile, assemble
import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'

# Load IBM Quantum account and set up service
service = QiskitRuntimeService(
    channel='ibm_quantum',
    token='efaee3112cb68eb568bde505587ca5c445cb28d0469c0704bd13d947fa7d9b4ece88e056397209eba60e573d1abf966d721132824147d841b90c3de33e8ff817'
)

# Function to interact with OpenAI GPT-4
def ask_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Function to run a quantum circuit
def run_quantum_circuit(circuit, backend_name):
    backend = service.backend(backend_name)
    transpiled_circuit = transpile(circuit, backend)
    qobj = assemble(transpiled_circuit)
    job = backend.run(qobj)
    result = job.result()
    return result

# Streamlit app
def main():
    st.title("Quantum AI Assistant")
    query = st.text_input("Enter your question:")
    
    if query:
        with st.spinner("Running quantum circuit..."):
            # Create a simple quantum circuit
            circuit = QuantumCircuit(1, 1)
            circuit.h(0)
            circuit.measure(0, 0)
            result = run_quantum_circuit(circuit, 'ibmq_qasm_simulator')
            st.write(f"Quantum result: {result.get_counts()}")

        with st.spinner("Getting AI response..."):
            ai_response = ask_gpt4(query)
            st.write(f"AI response: {ai_response}")

if __name__ == "__main__":
    main()
