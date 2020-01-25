from Space.Teleporter import Teleporter
from Space.Communicator import Communicator
#from JobRunner.SimulatorJobRunner import SimulatorJobRunner as JobRunner
from JobRunner.IBMQJobRunner import IBMQJobRunner as JobRunner
import time


class StarTrek:
    """To boldy quantum where no circuit has been before"""

    DEBUG = False

    def __init__(self, debug=False):
        self.DEBUG = debug
        self.communicator = Communicator(Teleporter(), JobRunner())

    def earth_to_enterprise(self, message):
        return self.communicator.send_and_receive(message)


print('Star Trek: Teleporting')
startrek = StarTrek()
send_message = 'To boldly go...'
start_time = time.time()
received_message = startrek.earth_to_enterprise(send_message)
end_time = time.time()
if received_message == send_message:
    diff_seconds = end_time - start_time
    print("Successfully sent message in", diff_seconds, "seconds =", diff_seconds / 60, "minutes")
else:
    print("Received a different message:", received_message)
