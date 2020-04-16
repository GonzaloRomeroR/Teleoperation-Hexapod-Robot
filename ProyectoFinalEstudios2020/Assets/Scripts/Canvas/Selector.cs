using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Selector : MonoBehaviour
{
    GameObject _toggleView;
    GameObject _toggleJoystick;
    GameObject _toggleSet;
    GameObject _toggleMove;
    GameObject _toggleUneven;

    GameObject _menuShow;
    GameObject _joystick;
    GameObject _menuSet;
    GameObject _joystickMove;
    GameObject _clockwiseButton;
    GameObject _anticlockwiseButton;


    public void Start()
    {
        _toggleView = GameObject.Find("ToggleView");
        _toggleJoystick = GameObject.Find("ToggleJoystick");
        _toggleSet = GameObject.Find("ToggleSet");
        _toggleMove = GameObject.Find("ToggleMove");
        _toggleUneven = GameObject.Find("ToggleUneven");

        _menuShow = GameObject.Find("MenuShow");
        _joystick = GameObject.Find("JoystickCam");
        _menuSet = GameObject.Find("MenuSet");
        _joystickMove = GameObject.Find("JoystickMove");
        _clockwiseButton = GameObject.Find("Clockwise");
        _anticlockwiseButton = GameObject.Find("Anticlockwise");

        _menuSet.SetActive(false);
        _joystickMove.SetActive(false);
        _clockwiseButton.SetActive(false);
        _anticlockwiseButton.SetActive(false);
    }

    public void OnToggle_View()
    {
        if (_toggleView.GetComponent<Toggle>().isOn == false)
        {
            _menuShow.SetActive(false);
        }
        else{
            _menuShow.SetActive(true);
        }
    }

    public void OnToggle_Joystick()
    {
        if (_toggleJoystick.GetComponent<Toggle>().isOn == false)
        {
            _joystick.SetActive(false);
        }
        else
        {
            _joystick.SetActive(true);
        }

    }

    public void OnToggle_Set()
    {
        if (_toggleSet.GetComponent<Toggle>().isOn == false)
        {
            _menuSet.SetActive(false);
        }
        else
        {
            _menuSet.SetActive(true);
        }

    }

    public void OnToggle_Uneven()
    {
        if (_toggleUneven.GetComponent<Toggle>().isOn == true)
        {
            Global.Instance.uneven = true;
        }
        else
        {
            Global.Instance.uneven = false;

        }
    }

    public void OnToggle_Move()
    {
        if (_toggleMove.GetComponent<Toggle>().isOn == false)
        {
            _joystickMove.SetActive(false);
            _clockwiseButton.SetActive(false);
            _anticlockwiseButton.SetActive(false); 

        }
        else
        {
            _joystickMove.SetActive(true);
            _clockwiseButton.SetActive(true);
            _anticlockwiseButton.SetActive(true);
            Global.Instance.MoveToZero();
        }

    }
}
