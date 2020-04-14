using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RobotMovement : MonoBehaviour
{

    public Joystick joystick;
    public RobotMathematics robotMath;

    private float angle;
    private float module;

    public float l1 = 28.5f;
    public float l2 = 75.5f;
    public float l3 = 129.8f;


    private void Update()
    {
        //print(GetJoystickInputAngle());
        //print(GetJoystickInputModule());
    }

    public float GetJoystickInputModule()
    {
        module = (float)Math.Pow(Math.Pow(joystick.Vertical, 2) + Math.Pow(joystick.Horizontal, 2), 0.5);
        return module;
    }

    public float GetJoystickInputAngle()
    {
        //angle = (float)Math.Atan2(joystick.Vertical, joystick.Horizontal) * 180f / (float)Math.PI;
        angle = (float)Math.Atan2(joystick.Vertical, joystick.Horizontal);
        return angle;
    }


    public float[] GetWalkingIncrements(float dL, float alpha, float direction, int leg)
    {
        float dX = dL * (float)Math.Cos(direction);
        float dY = dL * (float)Math.Sin(direction);

        float dx = dX * (float)Math.Cos(alpha + Math.PI / 3f * leg) + dY * (float)Math.Sin(alpha + Math.PI / 3f * leg);
        float dy = dY * (float)Math.Cos(alpha + Math.PI / 3f * leg) - dX * (float)Math.Sin(alpha + Math.PI / 3f * leg);

        return new float[] { dx, dy };

    }


    public float[][] GetWalkingCycle(float x0, float y0, float z0, float h, float dx, float dy, bool even)
    {


        if (even == true)
        {
            float[] lx = { x0, x0 + dx / 4, x0 + dx / 2, x0 + dx / 4, x0 };
            float[] ly = { y0, y0 + dy / 4, y0 + dy / 2, y0 + dy / 4, y0 };
            float[] lz = { z0, z0, z0, z0 + h, z0 };
            return new float[][] { lx, ly, lz };
        }
        else
        {
            float[] lx = { x0, x0 - dx / 4, x0 - dx / 2, x0 - dx / 4, x0 };
            float[] ly = { y0, y0 - dy / 4, y0 - dy / 2, y0 - dy / 4, y0 };
            float[] lz = { z0, z0 + h, z0, z0, z0 };
            return new float[][] { lx, ly, lz };
        }

    }

    public float[][] GetRotateCycle(float x0, float y0, float z0, float h, bool direction, float da, bool even)
    {
        float lxx = l1 + l2;  // FIX THIS, PLATFORM RADIUS
        float dp = ((l1 + l2) + lxx) * (float) Math.Tan(da * Math.PI / 180f);

        if (direction == false)
        {
            dp = -dp;
        }

        if (even == true)
        {
            float[] lx = { x0, x0, x0, x0, x0 };
            float[] ly = { y0, y0 + dp / 4, y0 + dp / 2, y0 + dp / 4, y0 };
            float[] lz = { z0, z0, z0, z0 + h, z0 };
            return new float[][] { lx, ly, lz };
        }
        else
        {
            float[] lx = { x0, x0, x0, x0, x0 };
            float[] ly = { y0, y0 - dp / 4, y0 - dp / 2, y0 - dp / 4, y0 };
            float[] lz = { z0, z0 + h, z0, z0, z0 };
            return new float[][] { lx, ly, lz };
        }

    }



    public float[][] GetJointsWalkingCycle(float[] lx, float[] ly, float[] lz)
    {

        float[][] trajectories = new float[lx.Length][];

        for (int i = 0; i < lx.Length; i++)
        {

            float[] angles = robotMath.LegInverseKinematics(lx[i], ly[i], lz[i], l1, l2, l3);

            trajectories[i] = angles;
        }

        float[] theta1 = new float[lx.Length];
        float[] theta2 = new float[lx.Length];
        float[] theta3 = new float[lx.Length];

        for (int i = 0; i < lx.Length; i++)
        {
            theta1[i] = trajectories[i][0];
            theta2[i] = trajectories[i][1];
            theta3[i] = trajectories[i][2];
        }

        return new float[][] { theta1, theta2, theta3};

    }

}
