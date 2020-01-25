from qiskit import execute, Aer
from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor


class IBMQJobRunner:
    DEBUG = False

    def __init__(self, n_shots=512):
        self.n_shots = n_shots
        IBMQ.load_account()

    def run(self, send_circuit):
        provider = IBMQ.get_provider(hub='ibm-q')
        backend = least_busy(provider.backends(simulator=False, n_qubits=5))
        print("Using provider", provider, "backend", backend)
        job_exp = execute(send_circuit, backend=backend, shots=self.n_shots)
        job_monitor(job_exp)
        return job_exp.result()
