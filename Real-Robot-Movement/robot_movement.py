import math
from robot_math import RobotMath

robotMath = RobotMath()

class RobotMovement():

    def get_walking_increments(self, dL, alpha, direction, leg):

        dX = dL * math.cos(direction)
        dY = dL * math.sin(direction)

        dx = dX * math.cos(alpha + math.pi / 3.0 * leg) + dY * math.sin(alpha + math.pi / 3.0 * leg)
        dy = dY * math.cos(alpha + math.pi / 3.0 * leg) - dX * math.sin(alpha + math.pi / 3.0 * leg)

        return dx, dy


    def get_walking_cycle(self, x0, y0, z0, h, dx, dy, even):
        if even:
            lx = [x0, x0 + dx / 4.0, x0 + dx / 2.0, x0 + dx / 4.0, x0 ]
            ly = [y0, y0 + dy / 4.0, y0 + dy / 2.0, y0 + dy / 4.0, y0 ]
            lz = [z0, z0, z0, z0 + h, z0]
            return lx, ly, lz
        else:
            lx = [x0, x0 - dx / 4.0, x0 - dx / 2.0, x0 - dx / 4.0, x0 ]
            ly = [y0, y0 - dy / 4.0, y0 - dy / 2.0, y0 - dy / 4.0, y0 ]
            lz = [z0, z0 + h, z0, z0, z0]
            return [lx, ly, lz]


    def get_joints_walking_cycle(self, lx, ly, lz, l1, l2, l3):

        trajectories = []
        for i in range(len(lx)):
            trajectories.append(robotMath.leg_inverse_kinematics(lx[i], ly[i], lz[i], l1, l2, l3))

        theta1 = []
        theta2 = []
        theta3 = []

        for i in range(len(lx)):
            theta1.append(trajectories[i][0])
            theta2.append(trajectories[i][1])
            theta3.append(trajectories[i][2])

        return [theta1, theta2, theta3]