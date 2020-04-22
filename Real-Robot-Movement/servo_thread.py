from threading import Timer,Thread,Event
import time
import GUI

DEBUG = True
TIMER = 0.0

MAX_FREQUENCY = 2250
MIN_FREQUENCY = 500

if DEBUG == False:
    from adafruit_servokit import ServoKit
    kit = ServoKit(channels = 16)


class ServoSetter(Thread):
    
    def __init__(self, gl):
        Thread.__init__(self)
        self.gl = gl


        self.offset_0 = 120
        self.offset_1 = 115
        self.offset_2 = 150

        if DEBUG == False:
            self.set_servos_frequencies(MIN_FREQUENCY, MAX_FREQUENCY);


    def set_servos_frequencies(self, min, max):
        for i in range(16):
            kit.servo[i].set_pulse_width_range(min, max)



    def run(self):
        while 1:
            if DEBUG == True:
                self.gl.walking_input(0.0)
                print(self.gl.commands)
                time.sleep(TIMER)
            
            else:
                self.gl.walking_input(0.0)
                print(self.gl.commands)
                kit.servo[0].angle = self.gl.commands[0][0] + self.offset_0
                kit.servo[1].angle = -self.gl.commands[0][1] + self.offset_1
                kit.servo[2].angle = self.gl.commands[0][2] + self.offset_2

                kit.servo[3].angle = self.gl.commands[1][0] + self.offset_0
                kit.servo[4].angle = -self.gl.commands[1][1] + self.offset_1
                kit.servo[5].angle = self.gl.commands[1][2] + self.offset_2
                
                kit.servo[6].angle = self.gl.commands[2][0] + self.offset_0
                kit.servo[7].angle = -self.gl.commands[2][1] + self.offset_1
                kit.servo[8].angle = self.gl.commands[2][2] + self.offset_2
                
                kit.servo[9].angle = self.gl.commands[3][0] + self.offset_0
                kit.servo[10].angle = -self.gl.commands[3][1] + self.offset_1
                kit.servo[11].angle = self.gl.commands[3][2] + self.offset_2
                
                kit.servo[12].angle = self.gl.commands[4][0] + self.offset_0
                kit.servo[13].angle = -self.gl.commands[4][1] + self.offset_1
                kit.servo[14].angle = self.gl.commands[4][2] + self.offset_2
                
                kit.servo[15].angle = self.gl.commands[5][0] + self.offset_0
                
                ''' kit.servo[16].angle = -self.gl.commands[0][1] + self.offset_1
                kit.servo[17].angle = -self.gl.commands[0][2] + self.offset_2
                 '''
                
                time.sleep(TIMER)