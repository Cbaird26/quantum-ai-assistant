import openai
from qiskit import QuantumCircuit, transpile, execute
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import IBMQ, least_busy

# Set your API keys here
openai.api_key = 'sk-proj-rjQkZR2EpFXe0O6fQ0gjT3BlbkFJ57LMTOzYuycUalwgCQvp'
IBMQ.save_account('efaee3112cb68eb568bde505587ca5c445cb28d0469c0704bd13d947fa7d9b4ece88e056397209eba60e573d1abf966d721132824147d841b90c3de33e8ff817', overwrite=True)

def chatgpt_query(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def create_quantum_circuit():
    qc = QuantumCircuit(2)
    qc.h(0)  # Apply Hadamard gate to qubit 0
    qc.cx(0, 1)  # Apply CNOT gate between qubit 0 and 1
    qc.measure_all()
    return qc

def run_quantum_circuit():
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q')
    backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 2 and not x.configuration().simulator and x.status().operational==True))
    qc = create_quantum_circuit()
    qc_transpiled = transpile(qc, backend)
    job = execute(qc_transpiled, backend, shots=1024)
    
    print(f"Running on backend: {backend}")
    job_monitor(job)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

def chatgpt_quantum_assistant(prompt):
    response = chatgpt_query(prompt)
    
    if "run quantum task" in prompt.lower():
        counts = run_quantum_circuit()
        response += f"\nQuantum task completed. Result: {counts}"
    
    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        assistant_response = chatgpt_quantum_assistant(user_input)
        print(f"Assistant: {assistant_response}")
