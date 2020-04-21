import numpy as np 

class Global():


    def __init__(self):


        self.timers = []

        self.values = [
            [ [0.0, 180.0, 90.0, 180.0, 20.0],[0],[0] ],
            [ [0.0],[0.0],[0.0] ],
            [ [0.0],[0.0],[0.0] ],
            [ [0.0],[0.0],[0.0] ],
            [ [0.0],[0.0],[0.0, 180.0, 90.0, 180.0, 20.0] ],
            [ [0.0],[0.0],[0.0, 180.0, 90.0, 180.0, 20.0] ]
        ]

        self.times = [
            [ [1.0, 1.0, 1.0, 1.0, 1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0] ],
            [ [1.0],[1.0],[1.0, 1.0, 1.0, 1.0, 1.0] ],
            [ [1.0],[1.0],[1.0, 1.0, 1.0, 1.0, 1.0] ]
        ]

        self.value = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.t = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.maximum = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]

        self.minimum = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
            ]

        self.last_value = [
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ],
            [ 0.0, 0.0, 0.0 ]
        ]
        
        self.counter = [
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ]
        ]

        self.finished = [
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ]
        ]

        
        self.commands = [
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 0 ]
        ]



        
    def set_joint_trajectory(self, values, times, row, col):
        
        if self.finished[row][col] == True:
            self.last_value[row][col] = self.commands[row][col]
            self.times[row][col] = times
            self.values[row][col] = values
            self.counter[row][col] = 0
            self.finished[row][col] = False
            self.t[row][col] = 0.0




