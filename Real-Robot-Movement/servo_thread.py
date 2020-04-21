from threading import Timer,Thread,Event
import time
import GUI



class ServoSetter(Thread):
    
    def __init__(self, gl):
        Thread.__init__(self)
        self.gl = gl
    
    def run(self):
        while 1:
            print(self.gl.commands)
            time.sleep(0.3)
        