﻿using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class JointFemurMovement : MonoBehaviour
{

    private int _legNumber;

    public static float[] _lastValues = { 0f, 0f, 0f, 0f, 0f, 0f };

    private ArticulationBody articulation;

    static int[] _counter = new int[] { 0, 0, 0, 0, 0, 0 };

    public static float[][] _values = new float[][] {
        new float[]  { 0f },
        new float[]  { 0f },
        new float[]  { 0f },
        new float[]  { 0f },
        new float[]  { 0f },
        new float[]  { 0f }
    };

    public static bool[] _finished = { true, true, true, true, true, true };

    public static float[][] _times = new float[][] {
        new float[]  { 1 },
        new float[]  { 1 },
        new float[]  { 1 },
        new float[]  { 1 },
        new float[]  { 1 },
        new float[]  { 1 }
    };

    static float[] _value = new float[] { 0f, 0f, 0f, 0f, 0f, 0f };
    static float[] _t = new float[] { 0f, 0f, 0f, 0f, 0f, 0f };
    static float[] _minimum = new float[] { 0f, 0f, 0f, 0f, 0f, 0f };
    static float[] _maximum = new float[] { 0f, 0f, 0f, 0f, 0f, 0f };

    private void Start()
    {
        _legNumber = Global.Instance.FindLegNumber(gameObject, "Leg");
        articulation = GetComponent<ArticulationBody>();
    }

    //private void Update()
    //{



    //}
    public bool IsFinished()
    {
        if (_finished.Contains(false))
        {
            return false;
        }
        else
        {
            return true;
        }
    }


    private void Update()
    {
        //transform.localRotation =
        //   Quaternion.AngleAxis(90, Vector3.forward) *
        //   Quaternion.AngleAxis(-(Global.Instance.legs[_legNumber][1]), Vector3.up) *
        //   Quaternion.AngleAxis(0, Vector3.forward);

        var drive = articulation.xDrive;
        drive.target = (Global.Instance.legs[_legNumber][1]);
        articulation.xDrive = drive;
    }


    private void FixedUpdate()
    {
        if (!Global.Instance.uneven)
        {
            MoveFemur();
        }
        else
        {
            MoveFemurUneven();
        }
        

    }


    private void MoveFemur()
    {

        if (_counter[_legNumber] < _values[_legNumber].Length)
        {
            if (_counter[_legNumber] == 0)
            {
                _minimum[_legNumber] = _lastValues[_legNumber];
            }
            else
            {
                _minimum[_legNumber] = _values[_legNumber][_counter[_legNumber] - 1];
            }

            _maximum[_legNumber] = _values[_legNumber][_counter[_legNumber]];

            _value[_legNumber] = Mathf.Lerp(_minimum[_legNumber], _maximum[_legNumber], _t[_legNumber]);

            _t[_legNumber] += 1f / _times[_legNumber][_counter[_legNumber]] * Time.fixedDeltaTime;


            if (_t[_legNumber] > 1.0f)
            {

                _counter[_legNumber]++;
                if (_counter[_legNumber] == _values[_legNumber].Length)
                {
                    _finished[_legNumber] = true;
                }
                _t[_legNumber] = 0.0f;
            }
            Global.Instance.legs[_legNumber][1] = _value[_legNumber];

        }
    }



    private void MoveFemurUneven()
    {

        if (_counter[_legNumber] < _values[_legNumber].Length)
        {
            if (_counter[_legNumber] == 0)
            {
                _minimum[_legNumber] = _lastValues[_legNumber];
            }
            else
            {
                _minimum[_legNumber] = _values[_legNumber][_counter[_legNumber] - 1];
            }

            _maximum[_legNumber] = _values[_legNumber][_counter[_legNumber]];

            _value[_legNumber] = Mathf.Lerp(_minimum[_legNumber], _maximum[_legNumber], _t[_legNumber]);

            _t[_legNumber] += 1f / _times[_legNumber][_counter[_legNumber]] * Time.fixedDeltaTime;


            if (_t[_legNumber] > 1.0f)
            {

                if (_legNumber % 2 == 0 && Global.Instance.legsContact[_legNumber] && _counter[_legNumber] == 4)
                {
                    _values[_legNumber][_counter[_legNumber]] = Global.Instance.legs[_legNumber][1];
                }

                if (_legNumber % 2 == 1 && Global.Instance.legsContact[_legNumber] && _counter[_legNumber] == 2)
                {
                    _values[_legNumber][_counter[_legNumber]] = Global.Instance.legs[_legNumber][1];
                }

                _counter[_legNumber]++;
                if (_counter[_legNumber] == _values[_legNumber].Length)
                {
                    _finished[_legNumber] = true;
                }
                _t[_legNumber] = 0.0f;

                return;
            }

            if (_legNumber % 2 == 0 && Global.Instance.legsContact[_legNumber] && _counter[_legNumber] == 4)
            {
                return;
            }

            if (_legNumber % 2 == 1 && Global.Instance.legsContact[_legNumber] && _counter[_legNumber] == 2)
            {
                return;
            }

            Global.Instance.legs[_legNumber][1] = _value[_legNumber];

        }
    }



    public void SetTrajectoryFemur(float[] values, float[] times, int leg)
    {

        _lastValues[leg] = Global.Instance.legs[leg][1];
        _values[leg] = values;
        _times[leg] = times;
        _finished[leg] = false;
        _counter[leg] = 0;
        _t[leg] = 0.0f;


    }
}


