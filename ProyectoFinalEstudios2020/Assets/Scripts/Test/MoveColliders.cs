using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveColliders : MonoBehaviour
{
    public BoxCollider boxCollider1;
    public BoxCollider boxCollider2;
    public BoxCollider boxCollider3;
    public BoxCollider boxCollider4;
    public BoxCollider boxCollider5;
    public BoxCollider boxCollider6;

    public Transform robotPosition;

    public GameObject cube1;
    public GameObject cube2;
    public GameObject cube3;
    public GameObject cube4;
    public GameObject cube5;
    public GameObject cube6;
    
    void FixedUpdate()
    {

        boxCollider1.center = 2 * new Vector3(
            cube1.transform.position.x - robotPosition.transform.position.x,
            cube1.transform.position.y - robotPosition.transform.position.y,
            cube1.transform.position.z - robotPosition.transform.position.z);

        boxCollider2.center = 2 * new Vector3(
            cube2.transform.position.x - robotPosition.transform.position.x,
            cube2.transform.position.y - robotPosition.transform.position.y,
            cube2.transform.position.z - robotPosition.transform.position.z);

        boxCollider3.center = 2 * new Vector3(
            cube3.transform.position.x - robotPosition.transform.position.x,
            cube3.transform.position.y - robotPosition.transform.position.y,
            cube3.transform.position.z - robotPosition.transform.position.z);

        boxCollider4.center = 2 * new Vector3(
            cube4.transform.position.x - robotPosition.transform.position.x,
            cube4.transform.position.y - robotPosition.transform.position.y,
            cube4.transform.position.z - robotPosition.transform.position.z);

        boxCollider5.center = 2 * new Vector3(
            cube5.transform.position.x - robotPosition.transform.position.x,
            cube5.transform.position.y - robotPosition.transform.position.y,
            cube5.transform.position.z - robotPosition.transform.position.z);

        boxCollider6.center = 2 * new Vector3(
            cube6.transform.position.x - robotPosition.transform.position.x,
            cube6.transform.position.y - robotPosition.transform.position.y,
            cube6.transform.position.z - robotPosition.transform.position.z);

        //boxCollider1.center = cube1.transform.position + robotPosition.transform.position;


    }
}
