from Adafruit_MotorHAT import Adafruit_MotorHAT
import time

MoHat = Adafruit_MotorHAT()
MotorLeft = MoHat.getMotor(1)
MotorRight = MoHat.getMotor(2)
MOTORSPEED = 100

def move_forward():
    MotorLeft.setSpeed(MOTORSPEED)
    MotorRight.setSpeed(MOTORSPEED)
    MotorRight.run(MoHat.FORWARD)
    MotorLeft.run(MoHat.FORWARD)
    time.sleep(1)

def move_backward():
    MotorLeft.setSpeed(MOTORSPEED)
    MotorRight.setSpeed(MOTORSPEED)
    MotorRight.run(MoHat.BACKWARD)
    MotorLeft.run(MoHat.BACKWARD)
    time.sleep(1)

def pivotturn_right():
    MotorLeft.setSpeed(MOTORSPEED)
    MotorRight.setSpeed(MOTORSPEED)
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.BACKWARD)
    time.sleep(1)                  

def pivotturn_left():
    MotorLeft.setSpeed(MOTORSPEED)
    MotorRight.setSpeed(MOTORSPEED)
    MotorLeft.run(MoHat.BACKWARD)
    MotorRight.run(MoHat.FORWARD)
    time.sleep(1)

def swingturn_right():
    MotorLeft.setSpeed(MOTORSPEED)
    MotorRight.setSpeed(MOTORSPEED / 2)
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.FORWARD)
    time.sleep(1)

def swingturn_left():
    MotorLeft.setSpeed(MOTORSPEED / 2)
    MotorRight.setSpeed(MOTORSPEED)
    MotorLeft.run(MoHat.FORWARD)
    MotorRight.run(MoHat.FORWARD)
    time.sleep(1)

try:
    move_forward()
    time.sleep(1)
    pivotturn_right()
    move_backward()
    time.sleep(1)
    swingturn_left()
    while(True):
        pass
        
except(KeyboardInterrupt):
    MotorLeft.run(MoHat.RELEASE)
    MotorRight.run(MoHat.RELEASE)
    print "test"
        
                      
