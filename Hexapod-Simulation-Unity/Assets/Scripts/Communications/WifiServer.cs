using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.Threading;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Configuration;



public class WifiServer : MonoBehaviour
{

    static TcpListener listener;
    Socket soc;
    Stream s;
    StreamWriter sw;
    private Thread m_Thread = null;

    string chain;

    bool firstRun = true;


    void OnEnable()
    {
        m_Thread = new Thread(ConnectWifi);
        m_Thread.Start();

    }

    private void OnDisable()
    {
        soc.Close();
    }

    void ConnectWifi()
    {
        IPAddress ipaddress = IPAddress.Parse("0.0.0.0");

        if (firstRun == true)
        {
            listener = new TcpListener(ipaddress, 8080);
            listener.Start();
            print("Server mounted,  listening to port 8080");
            firstRun = false;
        }
        
        soc = listener.AcceptSocket();
        print("Connected");

        s = new NetworkStream(soc);
        sw = new StreamWriter(s);
        sw.AutoFlush = true;
    }


    string CreateChain(string tag, int value)
    {
        string my_chain = ":" + tag + value.ToString();
        while (my_chain.Length < 20)
        {
            my_chain = my_chain + "=";
        }
        return my_chain;
    }

    public void SendData(string tag, int value)
    {
        try
        {
            chain = CreateChain(tag, value);
            sw.WriteLine(chain);
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
  
    }

}
