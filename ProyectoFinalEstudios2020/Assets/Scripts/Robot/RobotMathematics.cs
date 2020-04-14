using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Double;

public class RobotMathematics : MonoBehaviour
{

    public GameObject robot;


    private void Start()
    {
        
    }


    public float[][] PlatformInverseKinematics(float x, float y, float z, float roll, float pitch, float yaw, float radius, float angle, float l1, float l2, float l3, float initialX, float initialZ)
    {
        float[][] angles = {
            new float[3] {0, 0, 0},
            new float[3] {0, 0, 0},
            new float[3] {0, 0, 0},
            new float[3] {0, 0, 0},
            new float[3] {0, 0, 0},
            new float[3] {0, 0, 0}
        };

        var M = Matrix<float>.Build;
        var V = Vector<float>.Build;


        float[] o = { x, y, z};
        var O = V.Dense(3);
        O[1] = o[1];
        O[2] = o[2];
        O[0] = o[0];


        float [][] r = {
            new float [3] { (float)(Math.Cos(yaw) * Math.Cos(pitch)), (float)(Math.Cos(yaw) * Math.Sin(pitch) * Math.Sin(roll) - Math.Sin(yaw) * Math.Cos(roll)), (float)(Math.Cos(yaw) * Math.Sin(pitch) * Math.Cos(roll) + Math.Sin(yaw) * Math.Sin(roll))},
            new float [3] { (float) (Math.Sin(yaw) * Math.Cos(pitch)), (float)(Math.Sin(yaw) * Math.Sin(pitch) * Math.Sin(roll) + Math.Cos(yaw) * Math.Cos(roll)), (float)(Math.Sin(yaw) * Math.Sin(pitch) * Math.Cos(roll) - Math.Cos(yaw) * Math.Sin(roll))},
            new float [3] { (float)(-Math.Sin(pitch)), (float)(Math.Cos(pitch) * Math.Sin(roll)), (float)(Math.Cos(pitch) * Math.Cos(roll))}
        };

        var R = M.DenseOfRowArrays(r[0], r[1], r[2]);


        float[][] s1 = {

            new float[3] {radius * (float) Math.Cos(angle), radius * (float) Math.Sin(angle), 0},
            new float[3] {radius * (float) Math.Cos(angle + Math.PI / 3), radius * (float) Math.Sin(angle + Math.PI / 3), 0},
            new float[3] {radius * (float) Math.Cos(angle + 2 * Math.PI / 3), radius * (float) Math.Sin (angle + 2 * Math.PI / 3), 0},
            new float[3] {radius * (float) Math.Cos(angle + Math.PI), radius * (float) Math.Sin(angle + Math.PI), 0},
            new float[3] {radius * (float) Math.Cos(angle + 4 * Math.PI / 3), radius * (float) Math.Sin(angle + 4 * Math.PI / 3), 0},
            new float[3] {radius * (float) Math.Cos(angle + 5 * Math.PI / 3), radius * (float) Math.Sin(angle + 5 * Math.PI / 3), 0},

        };

        var S1 = M.DenseOfColumnArrays(s1[0], s1[1], s1[2], s1[3], s1[4], s1[5]);


        float[][] u = {

            new float[3] {(initialX + radius) * (float) Math.Cos(angle), (initialX + radius) * (float) Math.Sin(angle), initialZ},
            new float[3] {(initialX + radius) * (float) Math.Cos(angle + Math.PI / 3), (initialX + radius) * (float) Math.Sin(angle + Math.PI / 3), initialZ},
            new float[3] {(initialX + radius) * (float) Math.Cos(angle + 2 * Math.PI / 3), (initialX + radius) * (float) Math.Sin (angle + 2 * Math.PI / 3), initialZ},
            new float[3] {(initialX + radius) * (float) Math.Cos(angle + Math.PI), (initialX + radius) * (float) Math.Sin(angle + Math.PI), initialZ},
            new float[3] {(initialX + radius) * (float) Math.Cos(angle + 4 * Math.PI / 3), (initialX + radius) * (float) Math.Sin(angle + 4 * Math.PI / 3), initialZ},
            new float[3] {(initialX + radius) * (float) Math.Cos(angle + 5 * Math.PI / 3), (initialX + radius) * (float) Math.Sin(angle + 5 * Math.PI / 3), initialZ},

        };

        var U = M.DenseOfColumnArrays(u[0], u[1], u[2], u[3], u[4], u[5]);

        var L = M.Dense(3, 6);
        var alpha = M.Dense(1, 6);
        var beta = M.Dense(1, 6);
        var gamma = M.Dense(1, 6);

        var S2 = M.Dense(3, 6);
        var LPV = M.Dense(3, 6);
        var LP = M.Dense(1, 6);

        for (int i = 0; i < 6; i++)
        {
            L.SetColumn(i, O + R * S1.Column(i) - U.Column(i));

            alpha[0, i] = (float) Math.Atan2(L[1, i], L[0, i]);

           
            S2[0, i] = S1[0, i] - l1 * (float) Math.Cos(alpha[0 ,i]);
            S2[1, i] = S1[1, i] - l1 * (float)Math.Sin(alpha[0, i]);
            S2[2, i] = S1[2, i];


            LPV.SetColumn(i, O + R * S2.Column(i) - U.Column(i));

            LP[0, i] = (float) LPV.Column(i).L2Norm();

            float p = (float)Math.Atan2(LPV[2, i], Math.Pow(Math.Pow(LPV[1, i], 2) + Math.Pow(LPV[0, i], 2), 0.5));
            float phi = (float)Math.Asin((LPV[2, i] - L[2, i]) / l1);
            beta[0, i] = (float)Math.Acos((Math.Pow(l2, 2) - Math.Pow(l3, 2) + Math.Pow(LP[0, i], 2)) / (2 * l2 * LP[0, i])) - (p + phi);
            gamma[0, i] = (float)(Math.PI - Math.Acos((Math.Pow(l2, 2) + Math.Pow(l3, 2) - Math.Pow(LP[0, i], 2)) / (2 * l2 * l3))) * -1f;

        }

        float increment = 0;
        for(int i = 0; i < 6; i++)
        {
            alpha[0, i] = alpha[0, i] + increment;
            increment = increment - (float)Math.PI / 3;
        }


        for (int i = 0; i < 6; i++)
        {
            angles[i][0] = alpha[0, i] * 180f / (float)Math.PI;

            if (angles[i][0] > 90)
            {
                angles[i][0] = angles[i][0] - 180;
            }
            if (angles[i][0] < -90)
            {
                angles[i][0] = angles[i][0] + 180;
            }


            angles[i][1] = beta[0, i] * 180f / (float)Math.PI;
            angles[i][2] = gamma[0, i] * 180f / (float)Math.PI;
        }


        return angles;
    }



    public float[] LegInverseKinematics(float x, float y, float z, float l1, float l2, float l3)
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

    }

}
