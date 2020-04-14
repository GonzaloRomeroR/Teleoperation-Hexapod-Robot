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

    void Start()
    {
        
    }


    void Update()
    {
        X.SetText(robotTransformation.position.x.ToString("n1"));
        Y.SetText(robotTransformation.position.y.ToString("n1"));
        Z.SetText(robotTransformation.position.z.ToString("n1"));

        Roll.SetText(robotTransformation.eulerAngles.x.ToString("n1"));
        Yaw.SetText(robotTransformation.eulerAngles.y.ToString("n1"));
        Pitch.SetText(robotTransformation.eulerAngles.z.ToString("n1"));
    }
}
