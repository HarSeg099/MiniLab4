from Sensors import *
from Motors import *

class Gate:
    """ Gate class def """

    def __init__(self, servoPin=15, pirPin=18, proxPin = 17):
        self._servo = Servo(pin=servoPin, name="Gate 1")
        self._pir = DigitalSensor(pin=pirPin, lowactive=False)
        self._prox = DigitalSensor(pin=proxPin)

    def open(self):
        self._servo.setAngle(90)

    def close(self):
        self._servo.setAngle(180)

    def motionDetected(self):
        return self._pir.tripped()

    def vehiclePresent(self):
        return self._prox.tripped()
