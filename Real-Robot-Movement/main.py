from threading import Timer,Thread,Event
import my_timer as tm
from my_global import Global
import numpy as np
import time
import GUI
import servo_thread as st
from wifi import WifiClient
from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager
import multiprocessing


TIMER_TIME = 0.01
ARTICULATION_NUMBER = 18


WIFI = False

start_time = time.time()

gl = Global()


""" def leg_process(gl, initial_position):
stop_flag = Event()
for i in range(initial_position, initial_position + 3):
    gl.set_timers(i, tm.MyTimer(stop_flag, TIMER_TIME, gl, i))
    gl.get_timers(i).start() """


def main():
    # Start timer
    stop_flag = Event()
    for i in range(18):
        gl.timers.append(tm.MyTimer(stop_flag, TIMER_TIME, gl, i))
        gl.timers[i].start()

    st.ServoSetter(gl).start()
    if WIFI == True:
        WifiClient(gl)
    else:
        GUI.runGUI(gl)



if __name__ == '__main__':


    """     BaseManager.register('Global', Global)
    manager = BaseManager()
    manager.start()
    gl = manager.Global()
    p = Process(target=leg_process, args=(gl, 0,))
    p.start()
    p.join() """
    
    main()