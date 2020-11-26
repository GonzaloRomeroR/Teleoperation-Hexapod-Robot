using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Global : MonoBehaviour
{

    
    public static Global Instance { get; private set; }


    public float[][] legs = new float[][] {
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 }
    };

    public bool uneven = false;

    public float[][] lastValuesUneven  = new float[][] {
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 },
        new float[3] { 0, 0, -90 }
    };



    public float[] platformAngles = { 0, 0, 0 };
    public float[] platformPosition = { 0, 0, 0 };

    public bool[] legsContact = { false, false, false, false, false, false };

    public GameObject tibias;
    public GameObject femurs;
    public GameObject coxas;

    public RobotMathematics robotMath;
    public RobotMovement robotMove;

    public float stepHigh = 60f;
    public float stepDistance = 80.0f;
    public float rotateStep = 30;

    public bool rotationDirection = true;

    public float walkAmplitude = 0;
    public float walkHigh = 0;

    public int planner_steps = 0;
    public float planner_angle = 0;

    private float X = 0;
    private float Y = 0;
    private float Z = 0;

    private float Roll = 0;
    private float Pitch = 0;
    private float Yaw = 0;

    private float coordinateX = 0;
    private float coordinateY = 0;

    private float velocity = 1.0f;

    private float auxStepDistance;
    private float auxStepHigh;
    private float auxVelocity;
    private float auxRotationStep;





    JointCoxaMovement coxa;
    JointFemurMovement femur;
    JointTibiaMovement tibia;


    GameObject _wifiServer;


    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        coxa = coxas.GetComponent<JointCoxaMovement>();
        femur = femurs.GetComponent<JointFemurMovement>();
        tibia = tibias.GetComponent<JointTibiaMovement>();

        _wifiServer = GameObject.Find("WifiServer");

    }


    public void SetLegsContact(int legNumber, bool contact)
    {
        legsContact[legNumber] = contact;

    }


    public void OnClick_ButtonClockwise()
    {
        rotationDirection = true;
        if (robotMove.joystick.isActiveAndEnabled)
        {

            if (coxa.IsFinished() && femur.IsFinished() && tibia.IsFinished())
            {
                Rotate(rotationDirection);

                if (_wifiServer != null)
                {
                    string tag = "R";
                    int data = 1;
                    _wifiServer.GetComponent<WifiServer>().SendData(tag, data);
                }

            }
        }
    }

    public void OnClick_ButtonAnticlockwise()
    {
        rotationDirection = false;
        if (robotMove.joystick.isActiveAndEnabled)
        {
                if (coxa.IsFinished() && femur.IsFinished() && tibia.IsFinished())
                {
                    Rotate(rotationDirection);

                    if (_wifiServer != null)
                    {
                        string tag = "R";
                        int data = 0;
                        _wifiServer.GetComponent<WifiServer>().SendData(tag, data);
                    }

            }
        }
    }



    public int FindLegNumber(GameObject childObject, string name)
    {
        Transform t = childObject.transform;
        while (t.parent != null)
        {
            if (t.parent.name.Contains(name))
            {
                int legNumber = (int)Char.GetNumericValue(t.parent.name[t.parent.name.Length - 1]);
                return legNumber - 1;
            }
            t = t.parent.transform;
        }
        Debug.Log("Error leg not found");
        return -1;
    }

    public int FindJointNumber(GameObject childObject)
    {
        string coxa = "Coxa";
        string femur = "Femur";
        string tibia = "Tibia";
        Transform t = childObject.transform;
        while (t.parent != null)
        {
            if (t.parent.name.Contains(coxa))
            {
                return 0;
            }
            if (t.parent.name.Contains(femur))
            {
                return 1;
            }
            if (t.parent.name.Contains(tibia))
            {
                return 2;
            }
            t = t.parent.transform;
        }
        Debug.Log("Error Joint not found");
        return 0;
    }

    public void OnSetInput_JointVariable(TMP_InputField input)
    {   

        int legNumber = FindLegNumber(input.gameObject, "Leg");
        int jointNumber = FindJointNumber(input.gameObject);
        float newJointValue = float.Parse(input.text);

        //legs[legNumber][jointNumber] = newJointValue;

        if (_wifiServer != null)
        {
            string tag = "J" + legNumber.ToString() + jointNumber.ToString();
            _wifiServer.GetComponent<WifiServer>().SendData(tag, Int32.Parse(input.text));
        }


        if (jointNumber == 0)
        {
            JointCoxaMovement coxa = coxas.GetComponent<JointCoxaMovement>();
            coxa.SetTrajectoryCoxa(new float[] { newJointValue }, new float[] { 1 }, legNumber);
        }

        if (jointNumber == 1)
        {
            JointFemurMovement femur = femurs.GetComponent<JointFemurMovement>();
            femur.SetTrajectoryFemur(new float[] { newJointValue }, new float[] { 1 }, legNumber);
        }

        if (jointNumber == 2)
        {
            JointTibiaMovement tibia = tibias.GetComponent<JointTibiaMovement>();
            tibia.SetTrajectoryTibia(new float[] { newJointValue }, new float[] { 1 }, legNumber);
        }
    }


    public void OnSetInput_Coordinates(TMP_InputField input)
    {
        if (input.name == "InputX")
        {
            coordinateX = float.Parse(input.text);

        }
        if (input.name == "InputY")
        {
            coordinateY = float.Parse(input.text);

        }
    }

    public void OnSetInput_StepDistance(TMP_InputField input)
    {     
        auxStepDistance = float.Parse(input.text);

    }

    public void OnSetInput_RotationStep(TMP_InputField input)
    {
        auxRotationStep = float.Parse(input.text);

    }

    public void OnSetInput_Velocity(TMP_InputField input)
    {
        auxVelocity = float.Parse(input.text);

    }


    public void OnSetInput_StepHigh(TMP_InputField input)
    {
        auxStepHigh = float.Parse(input.text);

    }


    public void SetVelocity()
    {
        
        velocity = auxVelocity;

        if (_wifiServer != null)
        {
            string tag = "V" + velocity.ToString();
            _wifiServer.GetComponent<WifiServer>().SendData(tag, 0);
        }
    }

    public void SetStepHigh()
    {
        stepHigh = auxStepHigh;

        if (_wifiServer != null)
        {
            string tag = "H";
            _wifiServer.GetComponent<WifiServer>().SendData(tag, (int)stepHigh);
        }
    }

    public void SetStepDistance()
    {
        stepDistance = auxStepDistance;
        if (_wifiServer != null)
        {
            string tag = "D";
            _wifiServer.GetComponent<WifiServer>().SendData(tag, (int)stepDistance);
        }
    }

    public void SetRotationStep()
    {
        rotateStep = auxRotationStep;
        if (_wifiServer != null)
        {
            string tag = "S";
            _wifiServer.GetComponent<WifiServer>().SendData(tag, (int)rotateStep);
        }
    }


    public void SetCartesianPosition()
    {
        if (_wifiServer != null)
        {
            string tag = "C" + coordinateX.ToString() + "," + coordinateY.ToString();
            _wifiServer.GetComponent<WifiServer>().SendData(tag, 0); 
        }

        MoveRobotTo(coordinateX, coordinateY);
    }

    public void OnSetInput_PlatformVariables(TMP_InputField input)
    {
        if(input.name == "InputYaw")
        {
            Yaw = float.Parse(input.text) * (float)Math.PI / 180f;
        }
        if (input.name == "InputRoll")
        {
            Roll = float.Parse(input.text) * (float)Math.PI / 180f;
        }
        if (input.name == "InputPitch")
        {
            Pitch = float.Parse(input.text) * (float)Math.PI / 180f;
        }
        if (input.name == "InputX")
        {
            X = float.Parse(input.text);
        }
        if (input.name == "InputY")
        {
            Y = float.Parse(input.text);
        }
        if (input.name == "InputZ")
        {
            Z = float.Parse(input.text);
        }
    }

    public void MoveRobotTo(float X, float Y)
    {
        planner_angle = (float)Math.Atan2(Y, X);
        float module = (float)Math.Pow(Math.Pow(X, 2) + Math.Pow(Y, 2), 0.5);
        planner_steps = (int)(module / stepDistance);
    }

    private void Update()
    {
        
        if (robotMove.joystick.isActiveAndEnabled)
        {
            if (robotMove.GetJoystickInputModule() > 0.8)
            {

                if (_wifiServer != null)
                {
                    string tag = "W";
                    int data = (int)(robotMove.GetJoystickInputAngle() * 180f / (float)Math.PI);
                    _wifiServer.GetComponent<WifiServer>().SendData(tag, data);
                }

                if (coxa.IsFinished() && femur.IsFinished() && tibia.IsFinished())
                {
                    planner_steps = 0;
                    Walk(robotMove.GetJoystickInputAngle());


                }
            }
            else
            {
                if (planner_steps > 0)
                {
                    if (coxa.IsFinished() && femur.IsFinished() && tibia.IsFinished())
                    {
                        Walk(planner_angle);
                        planner_steps--;

                    }
                }
            }
        }
    }


    public void Walk(float direction)
    {

        if (!uneven)
        {
            WalkEven(direction);



        }
        else
        {
            WalkUneven(direction);

        }
    }


    private void WalkUneven(float direction)
    {
        float[] timers = { 0.001f, 1 / velocity, 2 /velocity, 1 / velocity, 2 / velocity };

        for (int i = 0; i < 6; i++)
        {
            float[] increments = robotMove.GetWalkingIncrements(stepDistance, 0, direction, i);
            float[][] cartesian;
            if (i % 2 == 0)
            {
                cartesian = robotMove.GetWalkingCycleUneven(robotMove.l1 + robotMove.l2 + walkAmplitude, 0, -robotMove.l3 - walkHigh, stepHigh, increments[0], increments[1], true);
            }
            else
            {
                cartesian = robotMove.GetWalkingCycleUneven(robotMove.l1 + robotMove.l2 + walkAmplitude, 0, -robotMove.l3 - walkHigh, stepHigh, increments[0], increments[1], false);
            }

            float[][] jointsEven = robotMove.GetJointsWalkingCycleUneven(cartesian[0], cartesian[1], cartesian[2], i);

            bool notNan = true;

            for (int j = 0; j < jointsEven.Length; j++)
            {
                for (int k = 0; k < jointsEven[j].Length; k++)
                {
                    if (float.IsNaN(jointsEven[j][k])){
                        notNan = false;
                    }

                }
            }
            if (notNan)
            {
                coxa.SetTrajectoryCoxa(jointsEven[0], timers, i);
                femur.SetTrajectoryFemur(jointsEven[1], timers, i);
                tibia.SetTrajectoryTibia(jointsEven[2], timers, i);
            }
            else
            {
                print("Imposible to move, invalid commands");
            }

        }
    }


    private void WalkEven(float direction)
    {
        float[] timers = { 0.001f, 1 / velocity, 1 / velocity, 1 / velocity, 1 / velocity };

        for (int i = 0; i < 6; i++)
        {
            float[] increments = robotMove.GetWalkingIncrements(stepDistance, 0, direction, i);
            float[][] cartesian;
            if (i % 2 == 0)
            {
                cartesian = robotMove.GetWalkingCycle(robotMove.l1 + robotMove.l2 + walkAmplitude, 0, -robotMove.l3 - walkHigh, stepHigh, increments[0], increments[1], true);
            }
            else
            {
                cartesian = robotMove.GetWalkingCycle(robotMove.l1 + robotMove.l2 + walkAmplitude, 0, -robotMove.l3 - walkHigh, stepHigh, increments[0], increments[1], false);
            }

            float[][] jointsEven = robotMove.GetJointsWalkingCycle(cartesian[0], cartesian[1], cartesian[2]);


            bool notNan = true;

            for (int j = 0; j < jointsEven.Length; j++)
            {
                for (int k = 0; k < jointsEven[j].Length; k++)
                {
                    if (float.IsNaN(jointsEven[j][k]))
                    {
                        notNan = false;
                    }

                }
            }
            if (notNan)
            {
                coxa.SetTrajectoryCoxa(jointsEven[0], timers, i);
                femur.SetTrajectoryFemur(jointsEven[1], timers, i);
                tibia.SetTrajectoryTibia(jointsEven[2], timers, i);
            }
            else
            {
                print("Imposible to move, invalid commands");
            }

        }
    }

    public void SetPlatformLocation()
    {
        if (_wifiServer != null)
        {
            string tag = "P" + X.ToString() + "," + Y.ToString() + "," + Z.ToString() + "," + ((int)(Roll * 180f / (float) Math.PI)).ToString() + "," + ((int)(Pitch * 180f / (float)Math.PI)).ToString() + "," + ((int)(Yaw * 180f / (float)Math.PI)).ToString();
            _wifiServer.GetComponent<WifiServer>().SendData(tag, 0);  // FIX THIS, THE ZERO IS USELESS
        }

        float[][] angles = robotMath.PlatformInverseKinematics(X, Y, Z, Roll, 
            Pitch, Yaw, robotMove.l1 + robotMove.l2, 0,
            robotMove.l1, robotMove.l2, robotMove.l3, robotMove.l1 + robotMove.l2, -robotMove.l3);

        //for (int i = 0; i < 6; i++)
        //{
        //    print(angles[i][0].ToString() + ", " + angles[i][1].ToString() + "," + angles[i][1].ToString());
        //}
        bool notNan = true;

        for (int j = 0; j < angles.Length; j++)
        {
            for (int k = 0; k < angles[j].Length; k++)
            {
                if (float.IsNaN(angles[j][k]))
                {
                    notNan = false;
                }

            }
        }
        if (notNan)
        {
            for (int i = 0; i < 6; i++)
            {
                coxa.SetTrajectoryCoxa(new float[] { angles[i][0] }, new float[] { 1 }, i);
                femur.SetTrajectoryFemur(new float[] { angles[i][1] }, new float[] { 1 }, i);
                tibia.SetTrajectoryTibia(new float[] { angles[i][2] }, new float[] { 1 }, i);
            }
        }
        else
        {
            print("Commands impossible to reach");
        }
    }


    public void MoveToZero()
    {
        for (int i = 0; i < 6; i++)
        {
            coxa.SetTrajectoryCoxa(new float[] { 0 }, new float[] { 1 }, i);
            femur.SetTrajectoryFemur(new float[] { 0 }, new float[] { 1 }, i);
            tibia.SetTrajectoryTibia(new float[] { -90 }, new float[] { 1 }, i);
        }
    }



    public void Rotate(bool direction)
    {
        float[] timers = { 0.01f, 1 / velocity, 1 / velocity, 1 / velocity, 1 / velocity };

        for (int i = 0; i < 6; i++)
        {
            float[][] cartesian;
            if (i % 2 == 0)
            {
                cartesian = robotMove.GetRotateCycle(robotMove.l1 + robotMove.l2 + walkAmplitude, 0, -robotMove.l3 - walkHigh, stepHigh, direction, rotateStep, true);
            }
            else
            {
                cartesian = robotMove.GetRotateCycle(robotMove.l1 + robotMove.l2 + walkAmplitude, 0, -robotMove.l3 - walkHigh, stepHigh, direction, rotateStep, false);
            }

            float[][] jointsEven = robotMove.GetJointsWalkingCycle(cartesian[0], cartesian[1], cartesian[2]);

            bool notNan = true;

            for (int j = 0; j < jointsEven.Length; j++)
            {
                for (int k = 0; k < jointsEven[j].Length; k++)
                {
                    if (float.IsNaN(jointsEven[j][k]))
                    {
                        notNan = false;
                    }

                }
            }
            if (notNan)
            {
                coxa.SetTrajectoryCoxa(jointsEven[0], timers, i);
                femur.SetTrajectoryFemur(jointsEven[1], timers, i);
                tibia.SetTrajectoryTibia(jointsEven[2], timers, i);
            }
            else
            {
                print("Commands impossible to reach");
            }
        }

    }

}