import numpy as np 

class Global():
    def __init__(self):
        self.last_value = 0.0
        self.counter = 0
        self.values = [0.0, 180.0, 90.0, 180.0, 20.0]
        self.times = [1.0, 1.0, 1.0, 1.0, 1.0]
        self.value = 0.0
        self.t = 0.0
        self.minimum = 0.0
        self.maximum = 0.0
        self.finished = False

        self.leg_values  = np.zeros((6, 3), dtype = np.float_)