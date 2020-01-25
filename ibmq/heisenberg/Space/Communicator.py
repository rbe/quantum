from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
import operator


class Communicator:
    """Spiddi-beep"""

    DEBUG = False

    def __init__(self, teleporter, runner):
        self.teleporter = teleporter
        self.runner = runner

    def send_and_receive_bit(self, bit):
        if self.DEBUG:
            print("Alice: prepare state she wants to send to Bob")
        send_q = QuantumRegister(3, "q")
        send_c = ClassicalRegister(3, "c")
        send_circuit = QuantumCircuit(send_q, send_c, name="send_bit")
        if int(bit) == 1:
            send_circuit.x(send_q[0])
        print("Sending bit", bit)
        send_circuit += self.teleporter.circuit()
        if self.DEBUG:
            print(send_circuit)
        result = self.runner.run(send_circuit)
        measurement_result = result.get_counts(send_circuit)
        if self.DEBUG:
            print("Bob: Have a look at Bob's measaurement results", measurement_result)
        bobs_qubit = {
            '0': sum([v for k, v in measurement_result.items() if k.startswith('0')]),
            '1': sum([v for k, v in measurement_result.items() if k.startswith('1')])
        }
        error_rate_percent = 100 - (bobs_qubit[str(bit)] / (bobs_qubit['1'] + bobs_qubit['0']) * 100)
        print("Bobs qubit:", bobs_qubit, "the error rate is", error_rate_percent, "%")
        # Simulator: received_bit_list = [k for k, v in bobs_qubit.items() if v == n_shots]
        received_bit = max(bobs_qubit.items(), key=operator.itemgetter(1))[0]
        print("Received bit " + received_bit)
        return int(received_bit)

    def send_and_receive_char(self, char):
        char_bits = list(bin(int.from_bytes(char.encode(), 'big'))[2:])
        print("Sending " + char + ", bits=" + str(char_bits))
        received_bits = []
        for bit in char_bits:
            if self.DEBUG: print("Sending bit " + bit)
            received_bits.append(self.send_and_receive_bit(bit))
        return received_bits

    def send_and_receive(self, message):
        received_bytes = []
        for char in message:
            received_bytes.append(self.send_and_receive_char(char))
        print("Received bytes/bits: " + str(received_bytes))
        received_message = ''
        for byte in received_bytes:
            b = '0b' + ''.join(str(x) for x in byte)
            c = int(b, 2)
            received_message += c.to_bytes((c.bit_length() + 7) // 8, 'big').decode()
        return received_message
