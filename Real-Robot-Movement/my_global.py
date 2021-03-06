import numpy as np
import math
from robot_movement import RobotMovement
from robot_math import RobotMath

robotMovement = RobotMovement()
robotMath = RobotMath()

class Global():
    """
    Class that stores all the global variables and methods 
    in order to make the robot move.

    """


    def __init__(self, commands):

        self.commands = commands
        self.l1 = 28.5
        self.l2 = 75.5
        self.l3 = 129.8

        self.planner_angle = 0
        self.planner_steps = 0

        self.radius = self.l1 + self.l2

        self.step_distance = 120
        self.step_high = 60

        self.velocity = 1.0

        self.rotate_step = 20


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
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ]
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
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ],
            [ 0.0, 0.0, -90.0 ]
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

        self.platform_variables = [0, 0, 0, 0, 0, 0]

    def get_all_commands(self):
        return self.commands

    def set_rotation_step(self, value):
        self.rotate_step = value

    def set_step_distance(self, value):
        self.step_distance = value

    def set_velocity(self, value):
        self.velocity = value

    def set_step_height(self, value):
        self.step_high = value
            

    def set_commands(self, row, col, value):
        self.commands[(row * 3) + col] = value
    
    def get_commands(self, row, col):
        return self.commands[(row * 3) + col]
        
    def set_finished(self, row, col, value):
        self.finished[row][col] = value
    
    def get_finished(self, row, col):
        return self.finished[row][col]

    def set_counter(self, row, col, value):
        self.counter[row][col] = value

    def get_counter(self, row, col):
        return self.counter[row][col]

    def set_last_value(self, row, col, value):
        self.last_value[row][col] = value

    def get_last_value(self, row, col):
        return self.last_value[row][col]

    def set_minimum(self, row, col, value):
        self.minimum[row][col] = value

    def get_minimum(self, row, col):
        return self.minimum[row][col]

    def set_maximum(self, row, col, value):    
        self.maximum[row][col] = value

    def get_maximum(self, row, col):
        return self.maximum[row][col]

    def set_t(self, row, col, value):
        self.t[row][col] = value

    def get_t(self, row, col):
        return self.t[row][col]

    def set_times(self, row, col, value):
        self.times[row][col] = value

    def get_times(self, row, col):
        return self.times[row][col]

    def set_value(self, row, col, value):
            self.value[row][col] = value

    def get_value(self, row, col):
        return self.value[row][col]

    def set_values(self, row, col, value):
            self.values[row][col] = value

    def get_values(self, row, col):
        return self.values[row][col]

    def set_timers(self, index, value):
        self.timers[index] = value

    def get_timers(self, index):
        return self.timers[index]

    # def walk_finished(self):
    #     if False in self.finished:
    #         return False
    #     else:
    #         return True

    def walk_finished(self):
        for i in range(6):
            if False in self.finished[i]:
                return False
        return True

    def set_robot_movement(self, X, Y):
        self.planner_angle = math.atan2(Y, X)
        module = (Y ** 2 + X ** 2) ** 0.5
        self.planner_steps = int(module / self.step_distance)

    def set_joint_trajectory(self, values, times, row, col):

        if self.finished[row][col] == True:
            self.last_value[row][col] = self.commands[(row * 3) + col]
            self.times[row][col] = times
            self.values[row][col] = values
            self.counter[row][col] = 0
            self.finished[row][col] = False
            self.t[row][col] = 0.0



    def walking_input(self, direction):
        if self.walk_finished():
            self.walk(direction)


    def rotation_input(self, direction):
        if self.walk_finished():
            self.rotation(direction)


    def walk(self, direction):
        times = [0.1, 1.0, 1.0, 1.0, 1.0]
        times = [x / self.velocity for x in times]

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


    def platform_movement(self):
        angles = robotMath.platform_inverse_kinematics(self.platform_variables[0], self.platform_variables[1], \
            self.platform_variables[2], self.platform_variables[3], self.platform_variables[4], self.platform_variables[5],\
                self.l1 + self.l2, 0, self.l1, self.l2, self.l3, self.l1 + self.l2, -self.l3)

        for i in range(6):
            self.set_joint_trajectory([angles[i][0]], [1], i, 0)
            self.set_joint_trajectory([angles[i][1]], [1], i, 1)
            self.set_joint_trajectory([angles[i][2]], [1], i, 2)


    def rotation(self, direction):

        times = [0.1, 1.0, 1.0, 1.0, 1.0]
        times = [x / self.velocity for x in times]

        for i in range(6):
            cartesian = []
            if i % 2 == 0:
                cartesian = robotMovement.get_rotation_cycle(self.l1 + self.l2, 0, -self.l3, self.step_high, direction,\
                    self.rotate_step, True, self.radius, self.l1, self.l2, self.l3 )
            else:
                cartesian = robotMovement.get_rotation_cycle(self.l1 + self.l2, 0, -self.l3, self.step_high, direction,\
                    self.rotate_step, False, self.radius, self.l1, self.l2, self.l3 )

            joints = robotMovement.get_joints_walking_cycle(cartesian[0], cartesian[1], cartesian[2], self.l1, self.l2, self.l3)

            self.set_joint_trajectory(joints[0], times, i, 0)
            self.set_joint_trajectory(joints[1], times, i, 1)
            self.set_joint_trajectory(joints[2], times, i, 2)

