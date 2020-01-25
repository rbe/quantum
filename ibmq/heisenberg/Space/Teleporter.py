from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit


class Teleporter:
    """I am a quantum based teleporter"""

    DEBUG = False

    def __init__(self):
        self.base_reg, self.base_clreg, self.base_circuit = self.build_teleporter()

    def build_teleporter(self):
        q = QuantumRegister(3, "q")
        c = ClassicalRegister(3, "c")
        qc = QuantumCircuit(q, c, name="teleporter")
        if self.DEBUG:
            print("Alice: prepare state she wants to send to Bob")
        qc.barrier()
        if self.DEBUG:
            print("Generate entangled qubit pair between Alice and Bob")
        qc.h(q[1])
        qc.cx(q[1], q[2])
        qc.barrier()
        if self.DEBUG:
            print("Alice: Prepare qubits")
        qc.cx(q[0], q[1])
        qc.h(q[0])
        qc.barrier()
        if self.DEBUG:
            print("Bob: Apply final gates according to Alice qubits and measures his qubit")
        qc.cx(q[1], q[2])
        qc.cz(q[0], q[2])
        qc.barrier()
        qc.measure(q, c)
        if self.DEBUG:
            print(qc)
        return q, c, qc

    def circuit(self):
        return self.base_circuit
