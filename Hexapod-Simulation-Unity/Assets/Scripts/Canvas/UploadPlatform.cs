using System;
using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class UploadPlatform : MonoBehaviour
{
    public TextMeshProUGUI X;
    public TextMeshProUGUI Y;
    public TextMeshProUGUI Z;

    public TextMeshProUGUI Yaw;
    public TextMeshProUGUI Pitch;
    public TextMeshProUGUI Roll;

    public Transform robotTransformation;

    void Update()
    {
        X.SetText(robotTransformation.position.x.ToString("n2"));
        Y.SetText(robotTransformation.position.y.ToString("n2"));
        Z.SetText(robotTransformation.position.z.ToString("n2"));

        float qx = robotTransformation.rotation[0];
        float qy = robotTransformation.rotation[1];
        float qz = robotTransformation.rotation[2];
        float qw = robotTransformation.rotation[3];


        float[] eulerAngles = QuaterniumToEuler(qx, qy, qz, qw);
        
        Roll.SetText(eulerAngles[0].ToString("n2"));
        Pitch.SetText(eulerAngles[1].ToString("n2"));
        Yaw.SetText(eulerAngles[2].ToString("n2"));

    }

    public float[] QuaterniumToEuler(float qx, float qy, float qz, float qw)
    {
        float sinr_cosp = 2 * (qy * qw - qx * qz);
        float cosr_cosp = 1 - 2 * (qz * qz + qy * qy);
        float yaw = (float)Math.Atan2(sinr_cosp, cosr_cosp);

        float roll;
        float sinp = 2 * (qx * qy + qz * qw);
        roll = (float)Math.Asin(sinp);

        float siny_cosp = 2 * (qw * qx - qy * qz);
        float cosy_cosp = 1 - 2 * (qx * qx + qz * qz);
        float pitch = (float)Math.Atan2(siny_cosp, cosy_cosp) + 1.57f;
        return new float[] {roll, pitch, yaw };
    }
}
