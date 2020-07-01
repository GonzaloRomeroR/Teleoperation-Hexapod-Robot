from threading import Timer,Thread,Event

ARTICULATION_NUMBER = 18


class MyTimer(Thread):
    """
    Timers related with each joint. They perform a linear interpolation between
    a intial and final position each time they are called.

    Args:
        Thread ([class]): [Thread class]
    """

    def __init__(self, event, seconds, gl, joint_number):
        self.stopped = event
        self.seconds = seconds
        self.gl = gl
        self.row, self.column = self.get_list_index(joint_number)
        Thread.__init__(self)


    def get_list_index(self, joint_number):
        counter_row = 0
        counter_column = 0
        for i in range(ARTICULATION_NUMBER):

            if joint_number == i:
                return counter_row, counter_column

            counter_column = counter_column + 1
            if counter_column == 3:
                counter_column = 0
                counter_row = counter_row + 1


    def run(self):
        while not self.stopped.wait(self.seconds):
            self.timer_function()

    def timer_function(self):
        

        row = self.row
        col = self.column

        if self.gl.counter[row][col] < len(self.gl.values[row][col]):

            if self.gl.counter[row][col] == 0:
                self.gl.minimum[row][col] = self.gl.last_value[row][col]
            else:
                self.gl.minimum[row][col] = self.gl.values[row][col][self.gl.counter[row][col] - 1]

            self.gl.maximum[row][col] = self.gl.values[row][col][self.gl.counter[row][col]]
            self.gl.value[row][col] = (self.gl.maximum[row][col] - self.gl.minimum[row][col]) * self.gl.t[row][col] + self.gl.minimum[row][col]
            self.gl.t[row][col] = self.gl.t[row][col] + 1 / self.gl.times[row][col][self.gl.counter[row][col]] * self.seconds

            if self.gl.t[row][col] > 1.0:
                self.gl.counter[row][col] = self.gl.counter[row][col] + 1
                if self.gl.counter[row][col] == len(self.gl.values[row][col]):
                    self.gl.finished[row][col] = True
                self.gl.t[row][col] = 0

            self.gl.set_commands(row, col, int(self.gl.value[row][col]))
