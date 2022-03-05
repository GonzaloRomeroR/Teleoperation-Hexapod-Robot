import multiprocessing
import time
from multiprocessing import Manager, Process
from multiprocessing.managers import BaseManager
from threading import Event, Thread, Timer

import numpy as np

import GUI
import joint_timer as tm
import planner_timer as ptm
from my_global import Global
from servo_process import servo_run
from wifi import WifiClient

TIMER_TIME = 0.01
PLANNER_TIME = 0.2
ARTICULATION_NUMBER = 18
WIFI = True

start_time = time.time()


def main():
    manager = Manager()
    commands = manager.list()
    for i in range(18):
        commands.append(0)

    commands[2] = -90
    commands[5] = -90
    commands[8] = -90
    commands[11] = -90
    commands[14] = -90
    commands[17] = -90

    gl = Global(commands)

    # Start timer
    stop_flag = Event()
    for i in range(18):
        gl.timers.append(tm.MyTimer(stop_flag, TIMER_TIME, gl, i))
        gl.timers[i].start()

    plan_timer = ptm.PlannerTimer(stop_flag, PLANNER_TIME, gl)
    plan_timer.start()

    p = Process(target=servo_run, args=(commands,))
    p.start()

    if WIFI == True:
        WifiClient(gl)
    else:
        GUI.runGUI(gl)
    p.join()


if __name__ == "__main__":
    main()
