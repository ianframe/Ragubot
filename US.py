import pigpio, eyw2
import numpy as np

class US:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        this.readings = [128, 128, 128, 128, 128]

    def get_distanc( ):
        distance = read_ultrasonic_sensor(trig, echo)
        if (distance != null):
            readings.append(distance)
            readings.pop(0)
        return np.mean(readings) 

        



