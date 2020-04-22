import math


class RobotMath():

    def leg_inverse_kinematics(self, x, y, z, l1, l2, l3):

        theta1 = math.atan2(y, x)

        x0 = x - l1 * math.cos(theta1)
        y0 = y - l1 * math.sin(theta1)

        p2 = x0 ** 2 + y0 ** 2 + z ** 2

        theta2 = math.acos((-l3 ** 2 + l2 ** 2 + p2) / (2 * l2 * p2 ** 0.5)) + math.atan2(z, (x0 ** 2 + y0 ** 2) ** 0.5)

        theta3 = - math.acos((p2 - l2 ** 2 - l3 ** 2) / (2 * l2 * l3))

        theta1 = theta1 * 180.0 / math.pi;
        theta2 = theta2 * 180.0 / math.pi;
        theta3 = theta3 * 180.0 / math.pi;

        return [theta1, theta2, theta3]