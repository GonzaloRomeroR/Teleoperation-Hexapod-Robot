import math

def leg_inverse_kinematics(x, y, z, l1, l2, l3):

    theta1 = math.atan2(y, x)

    x0 = x - l1 * math.cos(theta1)
    y0 = y - l1 * math.sin(theta1)

    p2 = x0 ** 2 + y0 ** 2 + z ** 2

    theta2 = math.acos((-l3 ** 2 + l2 ** 2 + p2) / (2 * l2 * p2 ** 0.5)) + math.atan2(z, (x0 ** 2 + y0 ** 2) ** 0.5)

    theta3 = - math.acos((p2 - l2 ** 2 - l3 ** 2) / (2 * l2 * l3))

    theta1 = theta1 * 180.0 / math.pi;
    theta2 = theta2 * 180.0 / math.pi;
    theta3 = theta3 * 180.0 / math.pi;

    return theta1, theta2, theta3



l1 = 28.5
l2 = 75.5
l3 = 129.8

print(leg_inverse_kinematics(l1 + l2 + 50 , 0, -l3 + 50, l1, l2, l3))








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