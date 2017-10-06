import time
import pigpio
pi = pigpio.pi()
import os

pi.set_mode(17,pigpio.INPUT)
pi.set_pull_up_down(17,pigpio.PUD_UP)

detect_low = 0;

def shutdown():
    os.system("sudo shutdown -h now")

while(True):
    time.sleep(1)
    print pi.read(17)
    if pi.read(17) == 1:
        detect_low = 0
    else:
        detect_low += 1
        if (detect_low >= 5):
            shutdown()
            time.sleep(2)
