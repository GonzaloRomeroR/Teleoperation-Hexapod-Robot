from threading import Timer,Thread,Event
import my_timer as tm
from my_global import Global
import numpy as np
import time
import GUI
import servo_thread as st
from wifi import WifiClient

TIMER_TIME = 0.1
ARTICULATION_NUMBER = 18


WIFI = True

gl = Global()
start_time = time.time()


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
    main()