from threading import Timer,Thread,Event

ARTICULATION_NUMBER = 18


class PlannerTimer(Thread):
    
    def __init__(self, event, seconds, gl):
        self.seconds = seconds
        self.stopped = event
        self.gl = gl
        Thread.__init__(self)

    def run(self):
        while not self.stopped.wait(self.seconds):
            self.timer_function()

    def timer_function(self):
    
        if self.gl.planner_steps > 0:
            if self.gl.walk_finished():
                self.gl.walking_input(self.gl.planner_angle)              
                self.gl.planner_steps = self.gl.planner_steps - 1

