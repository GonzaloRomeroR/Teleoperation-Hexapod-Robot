import math

import numpy as np


class RobotMath:
    """
    Class that provides the methods to calculate the kinematics of the robot.
    Inverse kinematics of the robot and platform are provided.

    """

    def leg_inverse_kinematics(self, x, y, z, l1, l2, l3):
        theta1 = math.atan2(y, x)
        x0 = x - l1 * math.cos(theta1)
        y0 = y - l1 * math.sin(theta1)
        p2 = x0 ** 2 + y0 ** 2 + z ** 2

        theta2 = math.acos(
            (-(l3 ** 2) + l2 ** 2 + p2) / (2 * l2 * p2 ** 0.5)
        ) + math.atan2(z, (x0 ** 2 + y0 ** 2) ** 0.5)

        theta3 = -math.acos((p2 - l2 ** 2 - l3 ** 2) / (2 * l2 * l3))

        theta1 = theta1 * 180.0 / math.pi
        theta2 = theta2 * 180.0 / math.pi
        theta3 = theta3 * 180.0 / math.pi
        return [theta1, theta2, theta3]

    def platform_inverse_kinematics(
        self, x, y, z, roll, pitch, yaw, radius, angle, l1, l2, l3, initialX, initialZ
    ):

        roll = roll * math.pi / 180.0
        pitch = pitch * math.pi / 180.0
        yaw = yaw * math.pi / 180.0
        angles = [[0, 0, 0] for i in range(6)]
        O = np.transpose(np.array([x, y, z]))
        R = np.array(
            [
                [
                    math.cos(yaw) * math.cos(pitch),
                    math.cos(yaw) * math.sin(pitch) * math.sin(roll)
                    - math.sin(yaw) * math.cos(roll),
                    math.cos(yaw) * math.sin(pitch) * math.cos(roll)
                    + math.sin(yaw) * math.sin(roll),
                ],
                [
                    math.sin(yaw) * math.cos(pitch),
                    math.sin(yaw) * math.sin(pitch) * math.sin(roll)
                    + math.cos(yaw) * math.cos(roll),
                    math.sin(yaw) * math.sin(pitch) * math.cos(roll)
                    - math.cos(yaw) * math.sin(roll),
                ],
                [
                    -math.sin(pitch),
                    math.cos(pitch) * math.sin(roll),
                    math.cos(pitch) * math.cos(roll),
                ],
            ]
        )

        S1 = np.array(
            [
                [radius * math.cos(angle), radius * math.sin(angle), 0],
                [
                    radius * math.cos(angle + math.pi / 3),
                    radius * math.sin(angle + math.pi / 3),
                    0,
                ],
                [
                    radius * math.cos(angle + 2 * math.pi / 3),
                    radius * math.sin(angle + 2 * math.pi / 3),
                    0,
                ],
                [
                    radius * math.cos(angle + math.pi),
                    radius * math.sin(angle + math.pi),
                    0,
                ],
                [
                    radius * math.cos(angle + 4 * math.pi / 3),
                    radius * math.sin(angle + 4 * math.pi / 3),
                    0,
                ],
                [
                    radius * math.cos(angle + 5 * math.pi / 3),
                    radius * math.sin(angle + 5 * math.pi / 3),
                    0,
                ],
            ]
        )

        S1 = np.transpose(S1)
        U = np.array(
            [
                [
                    (initialX + radius) * math.cos(angle),
                    (initialX + radius) * math.sin(angle),
                    initialZ,
                ],
                [
                    (initialX + radius) * math.cos(angle + math.pi / 3),
                    (initialX + radius) * math.sin(angle + math.pi / 3),
                    initialZ,
                ],
                [
                    (initialX + radius) * math.cos(angle + 2 * math.pi / 3),
                    (initialX + radius) * math.sin(angle + 2 * math.pi / 3),
                    initialZ,
                ],
                [
                    (initialX + radius) * math.cos(angle + math.pi),
                    (initialX + radius) * math.sin(angle + math.pi),
                    initialZ,
                ],
                [
                    (initialX + radius) * math.cos(angle + 4 * math.pi / 3),
                    (initialX + radius) * math.sin(angle + 4 * math.pi / 3),
                    initialZ,
                ],
                [
                    (initialX + radius) * math.cos(angle + 5 * math.pi / 3),
                    (initialX + radius) * math.sin(angle + 5 * math.pi / 3),
                    initialZ,
                ],
            ]
        )
        U = np.transpose(U)
        L = np.zeros((3, 6))
        alpha = np.zeros((1, 6))
        beta = np.zeros((1, 6))
        gamma = np.zeros((1, 6))
        S2 = np.zeros((3, 6))
        LPV = np.zeros((3, 6))
        LP = np.zeros((1, 6))

        for i in range(6):
            L[:, i] = np.add(np.add(O, R.dot(S1[:, i])), -U[:, i])
            alpha[0, i] = math.atan2(L[1, i], L[0, i])

            S2[0, i] = S1[0, i] - l1 * math.cos(alpha[0, i])
            S2[1, i] = S1[1, i] - l1 * math.sin(alpha[0, i])
            S2[2, i] = S1[2, i]

            LPV[:, i] = np.add(np.add(O, R.dot(S2[:, i])), -U[:, i])
            LP[0, i] = np.linalg.norm(LPV[:, i])

            p = math.atan2(LPV[2, i], (LPV[1, i] ** 2 + LPV[0, i] ** 2) ** 0.5)
            phi = math.asin((LPV[2, i] - L[2, i]) / l1)
            beta[0, i] = math.acos(
                (l2 ** 2 - l3 ** 2 + LP[0, i] ** 2) / (2 * l2 * LP[0, i])
            ) - (p + phi)
            gamma[0, i] = (
                math.pi
                - math.acos((l2 ** 2 + l3 ** 2 - LP[0, i] ** 2) / (2 * l2 * l3)) * -1.0
            )

        increment = 0.0
        for i in range(6):
            alpha[0, i] = alpha[0, i] + increment
            increment = increment - math.pi / 3.0
        for i in range(6):
            angles[i][0] = alpha[0, i] * 180.0 / math.pi
            if angles[i][0] > 90:
                angles[i][0] = angles[i][0] - 180
            if angles[i][0] < -90:
                angles[i][0] = angles[i][0] + 180
            angles[i][1] = beta[0, i] * 180.0 / math.pi
            angles[i][2] = gamma[0, i] * 180.0 / math.pi - 360

        return angles
