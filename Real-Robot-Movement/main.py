from threading import Timer,Thread,Event
import my_timer as tm
from my_global import Global
import numpy as np
import time
import GUI

TIMER_TIME = 0.1
gl = Global()
start_time = time.time()

def timer_function():

    if gl.counter < len(gl.values):
        if gl.counter == 0:
            gl.minimum = gl.last_value
        else:
            gl.minimum = gl.values[gl.counter - 1]
        gl.maximum = gl.values[gl.counter]
        gl.value = (gl.maximum - gl.minimum) * gl.t + gl.minimum
        gl.t = gl.t + 1 / gl.times[gl.counter] * TIMER_TIME
        if gl.t > 1.0:
            gl.counter = gl.counter + 1
            if gl.counter == len(gl.values):
                gl.finished = True
            gl.t = 0
        print(int(gl.value))
    else:
        print(gl.leg_values)
        print("--- %s seconds ---" % (time.time() - start_time))
        exit(0)


def main():
    # Start timer
    stop_flag = Event()
    timer = tm.MyTimer(stop_flag, TIMER_TIME, timer_function)
    timer.start()
    GUI.runGUI()


if __name__ == '__main__':
    main()