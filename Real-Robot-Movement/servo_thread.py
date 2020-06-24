from threading import Timer,Thread,Event
import time
import GUI

DEBUG = False
TIMER = 0.01

MAX_FREQUENCY = 2250
MIN_FREQUENCY = 450

# TD8120
MAX_FREQUENCY = 2500
MIN_FREQUENCY = 500

# MG996R
MAX_FREQUENCY = 2550
MIN_FREQUENCY = 450


def servo_run(commands):
    if DEBUG == False:
        from adafruit_servokit import ServoKit
        kit = ServoKit(channels = 16)
        kit2 = ServoKit(channels = 16, address = 0x41)


    offsets = [
        [138, 80, 30],
        [138, 69, 30],
        [100, 69, 38],
        [127, 72, 40],
        [142, 75, 35],
        [138, 71, 40]
    ]

    if DEBUG == False:
        for i in range(16):
            kit.servo[i].set_pulse_width_range(MIN_FREQUENCY, MAX_FREQUENCY)
            kit2.servo[i].set_pulse_width_range(MIN_FREQUENCY, MAX_FREQUENCY)


    while 1:
        if DEBUG == True:
            #walking_input(0.0)
            print(commands)
            time.sleep(TIMER)

        else:
            #walking_input(0.0)
            print(commands)
            kit2.servo[0].angle = commands[0] + offsets[0][0]
            kit2.servo[1].angle = commands[1] + offsets[0][1]
            kit2.servo[2].angle = -commands[2] + offsets[0][2]

            kit2.servo[3].angle = commands[3] + offsets[1][0]
            kit2.servo[4].angle = commands[4] + offsets[1][1]
            kit2.servo[5].angle = -commands[5] + offsets[1][2]

            kit.servo[6].angle = commands[6] + offsets[2][0]
            kit.servo[7].angle = commands[7] + offsets[2][1]
            kit.servo[8].angle = -commands[8] + offsets[2][2]

            kit.servo[3].angle = commands[9] + offsets[3][0]
            kit.servo[4].angle = commands[10] + offsets[3][1]
            kit.servo[5].angle = -commands[11] + offsets[3][2]

            kit.servo[2].angle = commands[12] + offsets[4][0]
            kit.servo[1].angle = commands[13] + offsets[4][1]
            kit.servo[0].angle = -commands[14] + offsets[4][2]

            kit2.servo[6].angle = commands[15] + offsets[5][0]
            kit2.servo[7].angle = commands[16] + offsets[5][1]
            kit2.servo[8].angle = -commands[17] + offsets[5][2]
