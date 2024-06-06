import openai
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Options
from qiskit import QuantumCircuit, transpile
import streamlit as st

# Set your OpenAI API key
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'

# Load IBM Quantum account and set up service
service = QiskitRuntimeService(
    token='efaee3112cb68eb568bde505587ca5c445cb28d0469c0704bd13d947fa7d9b4ece88e056397209eba60e573d1abf966d721132824147d841b90c3de33e8ff817'
)

# Function to run a quantum circuit
def run_quantum_circuit(circuit, backend_name):
    backend = service.backend(backend_name)
    options = Options(optimization_level=3)
    with Session(service, backend=backend) as session:
        job = session.run(transpile(circuit, backend), options=options)
        result = job.result()
    return result.get_counts()

# Function to interact with OpenAI GPT-4
def ask_gpt4(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
    )
    return response.choices[0].message["content"].strip()

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
            available_backends = service.backends(filters=lambda b: b.status().operational and not b.configuration().simulator)
            if available_backends:
                selected_backend = available_backends[0].name
                quantum_result = run_quantum_circuit(qc, selected_backend)
                st.write(f"Quantum result: {quantum_result}")
            else:
                st.write("No operational non-simulator backends available.")
        else:
            ai_response = ask_gpt4(query)
            st.write(ai_response)

if __name__ == "__main__":
    main()
