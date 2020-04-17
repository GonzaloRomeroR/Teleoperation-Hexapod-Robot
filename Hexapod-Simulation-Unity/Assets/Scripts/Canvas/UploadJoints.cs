using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class UploadJoints : MonoBehaviour
{
    int legNumber;
    int jointNumber;

    //public TextMeshPro _text;

    public TextMeshProUGUI text;

    private void Start()
    {
        legNumber = Global.Instance.FindLegNumber(gameObject, "Leg");
        jointNumber = Global.Instance.FindJointNumber(gameObject);
    }

    void Update()
    {

        text.SetText(Global.Instance.legs[legNumber][jointNumber].ToString("n1"));

    }
}
