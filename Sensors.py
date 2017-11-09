"""
    Engineering Concepts III Robotic Docent

    File: Sensors.py (python 2.7.9)
    Date: 11/10/17
    
    AUTHORS INCLUDE YOUR NAME(S) HERE

    This Python module includes classes for the ultrasonic sensor and infrared sensors (Pololu QTR-8RC). 

"""
import eyw2, numpy, pigpio, time

pi = pigpio.pi()


######################  Class Definitions   ######################
class US:
    """
    A class for reading data from the grove ultrasonic sensors
    """

    def __init__(self, trig, echo, safe_distance):
        """
        Sets up a 5 element array, initialized to value of safe_distance. Assigns GPIO
        pins to TRIG and ECHO functions used by the ultrasonic ranger. 
           
        Args:
            trig: GPIO pin assignment
            echo: GPIO pin assignment
            safe_distance: Value of moving average below which robot will halt
        Returns:
            None
        Raises:
            IOError
        """
        self.trig = trig
        self.echo = echo
        self.readings = [safe_distance, safe_distance, safe_distance, safe_distance, safe_distance]

    def get_distance():
        distance = read_ultrasonic_sensor(self.trig, self.echo)
        if (distance != null):
            readings.append(distance)
            readings.pop(0)
        return np.mean(readings) 

class IR:
    """
    A class for reading data from the Pololu QTR-8RC IR sensor array.
    """
    # Desired output scale from the Pololu IR sensors.
    OUTPUT_SCALE = 100

    def __init__(self):
        """ 
        Initializes the IR sensor to use 3 of the 8 sensors. 
        Args:
            None
        Returns:
            None
        Raises:
            None
             
        """
        # Using only 3 of eight channels on the Pololu IR sense array
        SENS_R = 17  
        SENS_C = 10
        SENS_L = 5

        # Assign value for number of channels used. This
        # will be used for iterating over all the channel values.
        self.MAX_CHANNELS = 3

        # Create two dimensional list that will hold sensor readback values for each
        # sensor channel. The min and max readings for each channel will then be used to
        # calibrate that channel.
        self.cal_rdgs = [[], [], []]

        # Create lists for each of the elements in the cal_rdgs list.
        self.chan_list = [SENS_R, SENS_C, SENS_L]
        self.ir_m_list = [0,0,0]
        self.ir_b_list = [0,0,0]

        # Create list that will contain either 1's or 0's depending
        # on the value sensed by each of the 3 IR channels used. 
        # Must adjust depending on number of channels used.
        self.ir_val_list = [0,0,0]
        
        # The following two dimensional list will contain the last five analog readings of
        # the 3 IR channels used. Values will range between 0 and OUTPUT_SCALE.
        # This list will be used to determine if robot has veered left or
        # right after losing line.
        self.ir_vals_list =[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]


    def calibrate(self):
        """ 
        Takes data from the actual line and background that the robot will follow to determine
        the value for darkest and lightes regions. These will be converted to values
        between 0 and MAX_SCALE.
        Args:
            None
        Returns:
            None
        Raises:
            None
             
        """
 
        for n in range(2000):
            for i  in range(self.MAX_CHANNELS):
                # The following code sets a GPIO to output, drives a high, waits
                # 10 microseconds, then changes the GPIO channel to an input making sure
                # there is no pull up or pull down that would prematurely bleed off charge.
                # The time it takes for the channel to go low is measured. This time is inversely
                # proportional to the amount of IR impingent on the sensor.
                # Black lines will have a long delay ~ 3 milliseconds, light surfaces will have a short
                # delay ~ 10 microseconds.
                finish = 0
                pi.set_mode(self.chan_list[i],pigpio.OUTPUT)
                pi.write(self.chan_list[i], 1)
                time.sleep(.00001)
                pi.set_mode(self.chan_list[i],pigpio.INPUT)
                pi.set_pull_up_down(self.chan_list[i],pigpio.PUD_OFF)
                start = time.time()
                while pi.read(self.chan_list[i]) == 1:
                    finish = time.time()
                delay = finish - start
                # On light backgrounds the above loop may not be entered due to
                # the rapid decay of the "high" signal.
                # This results in a negative min value which will throw
                # off the interpolation. In this case set, delay to 0. 
                if delay < 0:
                    delay = 0
                    
                self.cal_rdgs[i].append(delay)

        for i in range(self.MAX_CHANNELS):
            max_val = max(self.cal_rdgs[i])   
            min_val = min(self.cal_rdgs[i])
            print  "max = ", max_val
            print  "min = ", min_val
            # Use the fact that, given two points of a straight line, the slope (m) and
            # y intercept (b) of the straight line can be computed. Once m and b are computed
            # any ir sensor reading (x) can be converted to a scale between 0 and OUTPUT_SCALE
            # using y = mx + b, where x is the sensor reading and y is the value between 0
            # and OUTPUT_SCALE.
            m = OUTPUT_SCALE/(max_val - min_val)
            self.ir_m_list[i] = m
            self.ir_b_list[i] = - m * min_val
            
        print "Calibration complete."

        def read(self):
        """
        Read values from IR sensors and converts them, using calibration constants determined
        calibration() function to a scale between 0 and MAC_SCALE.
        Args:
            None
        Returns:
            None
        Raises:
            None
             
        """
        for i in range(self.MAX_CHANNELS):
            # See calibration() for sensor read method.
            sens = self.chan_list[i]
            pi.set_mode(sens,pigpio.OUTPUT)
            pi.write(sens, 1)
            time.sleep(.00001)
            pi.set_mode(sens,pigpio.INPUT)
            pi.set_pull_up_down(sens,pigpio.PUD_OFF)
            finish = 0
            start = time.time()
            while pi.read(sens)== 1:
                finish = time.time()
            delay = finish - start
                
            # The following line employs the slope (m) and y intercept (b)
            # calibration constants deterimed in the calibration function.
            ir_val = delay * self.ir_m_list[i] + self.ir_b_list[i]

            if DEBUG == 1: print int(ir_val),
            # The threshold for high and low signals will vary within the range
            # of the selected output scale. 
            # ir_val > 40: worked for masking tap on green vinyl
            # ir_val > 20 works for electricians tape on white poster board.
            if ir_val > 20:
                ir_dig = 1
            else:
                ir_dig = 0
            del self.ir_vals_list[i][0]
            self.ir_vals_list[i].append(ir_val)
            self.ir_val_list[i] = ir_dig
        if DEBUG == 1: print ""
        return self.ir_val_list        
