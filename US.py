import pigpio, eyw2
import numpy as np

class US:
    def __init__(self, trig, echo, safe_distance):
        self.trig = trig
        self.echo = echo
        self.safe_distance = safe_distance
        this.readings = [128, 128, 128, 128, 128]

    def get_distance():
        distance = read_ultrasonic_sensor(trig, echo)
        if (distance != null):
            readings.append(distance)
            readings.pop(0)
        return np.mean(readings) 



