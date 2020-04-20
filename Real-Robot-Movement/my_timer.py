from threading import Timer,Thread,Event

class MyTimer(Thread):
    def __init__(self, event, seconds, timer_function):
        Thread.__init__(self)
        self.stopped = event
        self.seconds = seconds
        self.timer_function = timer_function

    def run(self):
        while not self.stopped.wait(self.seconds):
            self.timer_function()