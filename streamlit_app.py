import streamlit as st
from qiskit import IBMQ, QuantumCircuit, transpile, execute
import openai

# Load IBMQ account and set up provider
IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')

# Function to run a quantum circuit
def run_quantum_circuit(circuit, backend_name):
    backend = provider.get_backend(backend_name)
    compiled_circuit = transpile(circuit, backend)
    job = execute(compiled_circuit, backend)
    result = job.result()
    return result.get_counts()

# OpenAI API setup
openai.api_key = 'YOUR_OPENAI_API_KEY'

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
