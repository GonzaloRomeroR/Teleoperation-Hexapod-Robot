from threading import Timer, Thread, Event

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

    """
    Function that write the joint commands in the I2C bus in order to move the robot
    Args:
        commands ([list]): [Shared list between processes that stores the 18 joint commands]
    """

    if DEBUG == False:
        from adafruit_servokit import ServoKit

        kit = ServoKit(channels=16)
        kit2 = ServoKit(channels=16, address=0x41)

    offsets = [
        [138, 80, 30],
        [138, 69, 30],
        [100, 69, 38],
        [127, 72, 40],
        [142, 75, 35],
        [98, 71, 40],
    ]

    min_coxa = -25
    max_coxa = 25

    min_femur = -90
    max_femur = 90

    min_tibia = -160
    max_tibia = 0

    if DEBUG == False:
        for i in range(16):
            kit.servo[i].set_pulse_width_range(MIN_FREQUENCY, MAX_FREQUENCY)
            kit2.servo[i].set_pulse_width_range(MIN_FREQUENCY, MAX_FREQUENCY)

    while 1:
        if DEBUG == True:
            # walking_input(0.0)
            print(commands)
            time.sleep(TIMER)

        else:
            # walking_input(0.0)
            print(commands)
            try:
                if commands[0] >= min_coxa and commands[0] <= max_coxa:
                    kit2.servo[0].angle = commands[0] + offsets[0][0]
                if commands[1] >= min_femur and commands[1] <= max_femur:
                    kit2.servo[1].angle = commands[1] + offsets[0][1]
                if commands[2] >= min_tibia and commands[2] <= max_tibia:
                    kit2.servo[2].angle = -commands[2] + offsets[0][2]

                if commands[3] >= min_coxa and commands[3] <= max_coxa:
                    kit2.servo[3].angle = commands[3] + offsets[1][0]
                if commands[4] >= min_femur and commands[4] <= max_femur:
                    kit2.servo[4].angle = commands[4] + offsets[1][1]
                if commands[5] >= min_tibia and commands[5] <= max_tibia:
                    kit2.servo[5].angle = -commands[5] + offsets[1][2]

                if commands[6] >= min_coxa and commands[6] <= max_coxa:
                    kit.servo[6].angle = commands[6] + offsets[2][0]
                if commands[7] >= min_femur and commands[7] <= max_femur:
                    kit.servo[7].angle = commands[7] + offsets[2][1]
                if commands[8] >= min_tibia and commands[8] <= max_tibia:
                    kit.servo[8].angle = -commands[8] + offsets[2][2]

                if commands[9] >= min_coxa and commands[9] <= max_coxa:
                    kit.servo[3].angle = commands[9] + offsets[3][0]
                if commands[10] >= min_femur and commands[10] <= max_femur:
                    kit.servo[4].angle = commands[10] + offsets[3][1]
                if commands[11] >= min_tibia and commands[11] <= max_tibia:
                    kit.servo[5].angle = -commands[11] + offsets[3][2]

                if commands[12] >= min_coxa and commands[12] <= max_coxa:
                    kit.servo[2].angle = commands[12] + offsets[4][0]
                if commands[13] >= min_femur and commands[13] <= max_femur:
                    kit.servo[1].angle = commands[13] + offsets[4][1]
                if commands[14] >= min_tibia and commands[14] <= max_tibia:
                    kit.servo[0].angle = -commands[14] + offsets[4][2]

                if commands[15] >= min_coxa and commands[15] <= max_coxa:
                    kit2.servo[6].angle = commands[15] + offsets[5][0]
                if commands[16] >= min_femur and commands[16] <= max_femur:
                    kit2.servo[7].angle = commands[16] + offsets[5][1]
                if commands[17] >= min_tibia and commands[17] <= max_tibia:
                    kit2.servo[8].angle = -commands[17] + offsets[5][2]

            except:

                print("I2C error")
