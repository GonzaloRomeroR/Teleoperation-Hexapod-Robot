import numpy as np
from robot_movement import RobotMovement

robotMovement = RobotMovement()

class Global():


    def __init__(self):

        self.l1 = 28.5
        self.l2 = 75.5
        self.l3 = 129.8

        self.step_distance = 40
        self.step_high = 60


        self.timers = []

        self.values = [
            [ [0.0],[0.0],[-90.0] ],
            [ [0.0],[0.0],[-90.0] ],
            [ [0.0],[0.0],[-90.0] ],
            [ [0.0],[0.0],[-90.0] ],
            [ [0.0],[0.0],[-90.0] ],
            [ [0.0],[0.0],[-90.0] ]
        ]

        self.times = [
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ]
        ]

        self.value = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.t = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.maximum = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.minimum = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
            ]

        self.last_value = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.counter = [
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ]
        ]

        self.finished = [
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ]
        ]


        self.commands = [
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ]
        ]

    def walk_finished(self):
        if False in self.finished:
            return False
        else:
            return True

    def set_joint_trajectory(self, values, times, row, col):

        if self.finished[row][col] == True:
            self.last_value[row][col] = self.commands[row][col]
            self.times[row][col] = times
            self.values[row][col] = values
            self.counter[row][col] = 0
            self.finished[row][col] = False
            self.t[row][col] = 0.0



    def walking_input(self, direction):
        if self.walk_finished():
            self.walk(direction)


    def walk(self, direction):
        times = [1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(6):
            dx, dy = robotMovement.get_walking_increments(self.step_distance, 0, direction, i)
            cartesian = []
            if i % 2 == 0:
                cartesian = robotMovement.get_walking_cycle(self.l1 + self.l2, 0, -self.l3, self.step_high, dx, dy, True )
            else:
                cartesian = robotMovement.get_walking_cycle(self.l1 + self.l2, 0, -self.l3, self.step_high, dx, dy, False )

            joints = robotMovement.get_joints_walking_cycle(cartesian[0], cartesian[1], cartesian[2], self.l1, self.l2, self.l3)

            self.set_joint_trajectory(joints[0], times, i, 0)
            self.set_joint_trajectory(joints[1], times, i, 1)
            self.set_joint_trajectory(joints[2], times, i, 2)






