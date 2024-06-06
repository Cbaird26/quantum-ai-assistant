import openai
from qiskit_ibm_provider import IBMProvider, IBMProviderError
from qiskit import QuantumCircuit, transpile, assemble
import streamlit as st

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'

# Save and load IBMQ account using your API token
try:
    provider = IBMProvider(token='efaee3112cb68eb568bde505587ca5c445cb28d0469c0704bd13d947fa7d9b4ece88e056397209eba60e573d1abf966d721132824147d841b90c3de33e8ff817')
except IBMProviderError as e:
    st.error(f"Failed to load IBM Q account: {e}")

# Function to run a quantum circuit
def run_quantum_circuit(circuit, backend_name):
    backend = provider.get_backend(backend_name)
    compiled_circuit = transpile(circuit, backend)
    qobj = assemble(compiled_circuit)
    job = backend.run(qobj)
    result = job.result()
    return result.get_counts()

# Function to interact with OpenAI GPT-4
def ask_gpt4(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Quantum AI Assistant")
    
    query = st.text_input("Enter your question:")
    
    if st.button("Submit"):
        if 'quantum' in query.lower():
            # Example quantum circuit
            qc = QuantumCircuit(2, 2)
            qc.h(0)
            qc.cx(0, 1)
            qc.measure([0, 1], [0, 1])
            
            # Select an available backend
            available_backends = provider.backends(filters=lambda b: b.status().operational and not b.configuration().simulator)
            if available_backends:
                selected_backend = available_backends[0].name()
                quantum_result = run_quantum_circuit(qc, selected_backend)
                st.write(f"Quantum result: {quantum_result}")
            else:
                st.write("No operational non-simulator backends available.")
        else:
            ai_response = ask_gpt4(query)
            st.write(ai_response)

if __name__ == "__main__":
    main()
