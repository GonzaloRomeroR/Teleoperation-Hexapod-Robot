from threading import Timer,Thread,Event
import my_timer as tm
from my_global import Global
import numpy as np
import time
import GUI
from servo_thread import servo_run
from wifi import WifiClient
from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager
import multiprocessing


TIMER_TIME = 0.01
ARTICULATION_NUMBER = 18


WIFI = False

start_time = time.time()



def main():

    manager = Manager()
    commands = manager.list()
    for i in range(18):
        commands.append(0)
    gl = Global(commands)

    # Start timer
    stop_flag = Event()
    for i in range(18):
        gl.timers.append(tm.MyTimer(stop_flag, TIMER_TIME, gl, i))
        gl.timers[i].start()

    p = Process(target=servo_run, args=(commands,))
    p.start()
    

    if WIFI == True:
        WifiClient(gl)
    else:
        GUI.runGUI(gl)
    p.join()


if __name__ == '__main__':
    main()