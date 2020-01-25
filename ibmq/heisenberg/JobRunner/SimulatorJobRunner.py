from qiskit import execute, Aer


class SimulatorJobRunner:
    DEBUG = False

    def __init__(self, n_shots=1):
        self.n_shots = n_shots

    def run(self, send_circuit):
        if self.DEBUG:
            print("Simulating on QASM")
        qasm_backend = Aer.get_backend('qasm_simulator')
        job_sim = execute(send_circuit, qasm_backend, shots=self.n_shots)
        return job_sim.result()
