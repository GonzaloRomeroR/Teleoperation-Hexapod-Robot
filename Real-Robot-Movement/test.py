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


robot = RobotMovement()

l1 = 28.5;
l2 = 75.5;
l3 = 129.8;

a = robot.get_walking_increments(10, 0, 0, 0)
print(a)
b = robot.get_walking_cycle(l1 + l2, 0, -l3, 40, 10, 0 , False)
print(b)
c = robot.get_joints_walking_cycle(b[0], b[1], b[2], l1, l2, l3)
print(c)



''' public float[] LegInverseKinematics(float x, float y, float z, float l1, float l2, float l3)
{
    float[] jointsValues = new float[3];
    float theta1, theta2, theta3;
    float p2, x0, y0;

    theta1 = (float) Math.Atan2(y, x);

    x0 = x - l1 * (float)Math.Cos(theta1);
    y0 = y - l1 * (float)Math.Sin(theta1);

    p2 = (float) (Math.Pow(x0, 2) + Math.Pow(y0, 2) + Math.Pow(z, 2));


    theta2 = (float)Math.Acos((-Math.Pow(l3, 2) + Math.Pow(l2, 2) 
        + p2) /(2 * l2 * Math.Pow(p2, 0.5))) +
        (float) Math.Atan2( z, (Math.Pow((Math.Pow(x0, 2) + Math.Pow(y0, 2)), 0.5 )));


    theta3 = - (float) Math.Acos((p2 - Math.Pow(l2, 2) - Math.Pow(l3, 2)) / (2 * l2 * l3));


    jointsValues[0] = theta1 * 180f / (float) Math.PI;
    jointsValues[1] = theta2 * 180f / (float) Math.PI;
    jointsValues[2] = theta3 * 180f / (float) Math.PI;

    return jointsValues;

} '''