using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraMovement : MonoBehaviour
{

    public Joystick joystick;

    private Vector3 target = new Vector3(0.0f, 0.0f, 0.0f);

    void Update()
    {
        if (joystick != null)
        {

            //  Joystick variable X 
            if (joystick.Horizontal >= .2f)
            {
                transform.RotateAround(target, transform.up, 10 * Time.deltaTime);

            }
            else if (joystick.Horizontal <= -0.2f)
            {
                transform.RotateAround(target, transform.up, -10 * Time.deltaTime);
            }

            // Joystick variable y¿Y
            if (joystick.Vertical >= .2f)
            {
                transform.RotateAround(target, transform.right, 10 * Time.deltaTime);

            }
            else if (joystick.Vertical <= -.2f)
            {
                transform.RotateAround(target, -transform.right, 10 * Time.deltaTime);
            }


        }
    }
}
