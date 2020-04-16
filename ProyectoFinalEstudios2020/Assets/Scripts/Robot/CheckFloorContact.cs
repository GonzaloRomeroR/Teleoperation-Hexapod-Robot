using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CheckFloorContact : MonoBehaviour
{

    private int _legNumber;

    private void Start()
    {
        _legNumber = Global.Instance.FindLegNumber(gameObject, "Leg");
    }

    private void OnTriggerEnter(Collider other)
    {
        Global.Instance.SetLegsContact(_legNumber, true);
    }

    private void OnTriggerExit(Collider other)
    {
        Global.Instance.SetLegsContact(_legNumber, false);
    }
}
