using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using TMPro;

public class Stability : MonoBehaviour
{
    public GameObject platform;
    public GameObject endEffector1;
    public GameObject endEffector2;
    public GameObject endEffector3;
    public GameObject endEffector4;
    public GameObject endEffector5;
    public GameObject endEffector6;

    public TextMeshProUGUI text;

    Transform transformPlatform;

    Transform[] transforms = new Transform[6];

    List<float[]> contactPoints = new List<float[]>();

    // Start is called before the first frame update
    void Start()
    {
        transformPlatform = platform.GetComponent<Transform>();

        transforms[0] = endEffector1.GetComponent<Transform>();
        transforms[1] = endEffector2.GetComponent<Transform>();
        transforms[2] = endEffector3.GetComponent<Transform>();
        transforms[3] = endEffector4.GetComponent<Transform>();
        transforms[4] = endEffector5.GetComponent<Transform>();
        transforms[5] = endEffector6.GetComponent<Transform>();
    }

    // Update is called once per frame
    void Update()
    {
        int counter = 0;

        for (int i = 0; i < Global.Instance.legsContact.Length; i++)
        {
            if (Global.Instance.legsContact[i] == true)
            {
                counter++;
                float[] coordinates = new float[] { transforms[i].position.x, transforms[i].position.z };
                contactPoints.Add(coordinates);

            }
        }
        if (counter == 3)
        {
            float XCM = transformPlatform.position.x;
            float ZCM = transformPlatform.position.z;


            float XC1 = contactPoints[0][0];
            float ZC1 = contactPoints[0][1];
            float XC3 = contactPoints[1][0];
            float ZC3 = contactPoints[1][1];
            float XC5 = contactPoints[2][0];
            float ZC5 = contactPoints[2][1];




            //float S1 = 0.5f * ((XC1 - XCM) * (ZC3 - ZCM) - (XC3 - XCM) * (ZC1 - ZCM));
            //float S3 = 0.5f * ((XC3 - XCM) * (ZC5 - ZCM) - (XC5 - XCM) * (ZC3 - ZCM));
            //float S5 = 0.5f * ((XC5 - XCM) * (ZC1 - ZCM) - (XC1 - XCM) * (ZC5 - ZCM));

            float S1 = 0.5f * (Math.Abs((XC1 - XCM) * (ZC3 - ZCM)) + Math.Abs((XC3 - XCM) * (ZC1 - ZCM)));
            float S3 = 0.5f * (Math.Abs((XC3 - XCM) * (ZC5 - ZCM)) + Math.Abs((XC5 - XCM) * (ZC3 - ZCM)));
            float S5 = 0.5f * (Math.Abs((XC5 - XCM) * (ZC1 - ZCM) + Math.Abs((XC1 - XCM) * (ZC5 - ZCM))));

            float L1 = (float) Math.Pow(Math.Pow(XC3 - XC1, 2) + Math.Pow(ZC3 - ZC1, 2), 0.5);
            float L3 = (float) Math.Pow(Math.Pow(XC3 - XC5, 2) + Math.Pow(ZC3 - ZC5, 2), 0.5);
            float L5 = (float) Math.Pow(Math.Pow(XC5 - XC1, 2) + Math.Pow(ZC5 - ZC1, 2), 0.5);

            float d1 = 2 * S1 / L1;
            float d3 = 2 * S3 / L3;
            float d5 = 2 * S5 / L5;

            float[] smArray = new float[] { d1, d3, d5 };
            float SM = smArray.Min();
            float minIndex = Array.IndexOf(smArray, SM);

            contactPoints.Clear();

            text.SetText(SM.ToString("n2"));

        }
    }
}
