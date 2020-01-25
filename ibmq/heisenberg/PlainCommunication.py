from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from qiskit import execute, Aer


q = QuantumRegister(3, "q")
c = ClassicalRegister(3, "c")
qc = QuantumCircuit(q, c, name="teleport")
print("Alice: prepare state she wants to send to Bob")
# qc.h(q[0])
# qc.z(q[0])
qc.x(q[0])
# qc.barrier()
print("Generate the entangled pair between Alice and Bob")
qc.h(q[1])
qc.cx(q[1], q[2])
# qc.barrier()
print("Alice: Prepare qubits")
qc.cx(q[0], q[1])
qc.h(q[0])
# qc.barrier()
print("Bob: Apply final gates according to Alice qubits and measures his qubit")
qc.cx(q[1], q[2])
qc.cz(q[0], q[2])
# qc.barrier()
qc.measure(q, c)
print(qc)
#
print("Simulating on QASM")
qasm_backend = Aer.get_backend('qasm_simulator')
job_sim = execute(qc, qasm_backend, shots=1024)
sim_result = job_sim.result()
measurement_result = sim_result.get_counts(qc)
print(measurement_result)
print("Bob: Have a look at Bob's measaurement results")
bobs_qubit = {
    '0': sum([v for k, v in measurement_result.items() if k.startswith('0')]),
    '1': sum([v for k, v in measurement_result.items() if k.startswith('1')])
}
print(bobs_qubit)
# print("Bob: Remove the last measurement gate from the quantum circuit")
# qc.data.pop(-1)
# print("Bob: Add reverse secret unitary and measurment")
# qc.z(q[2])
# qc.h(q[2])
# qc.measure(q[2], c[2])
# print(qc)
#
# print("Simulating on QASM")
# qasm_backend = Aer.get_backend('qasm_simulator')
# job_sim = execute(qc, qasm_backend, shots=1024)
# sim_result = job_sim.result()
# measurement_result = sim_result.get_counts(qc)
# print(measurement_result)
# print("Bob: Have a look at Bob's measaurement results")
# bobs_qubit = {
#    '0': sum([v for k, v in measurement_result.items() if k.startswith('0')]),
#    '1': sum([v for k, v in measurement_result.items() if k.startswith('1')])
# }
# print(bobs_qubit)
