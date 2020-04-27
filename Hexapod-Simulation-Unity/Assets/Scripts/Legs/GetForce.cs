using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GetForce : MonoBehaviour
{

    private ArticulationBody articulation;


    void Start()
    {
        articulation = GetComponent<ArticulationBody>();
    }

    void Update()
    {
        ArticulationReducedSpace a = articulation.jointAcceleration;
        //print(a.dofCount);
        print(a[0]);

    }
}
