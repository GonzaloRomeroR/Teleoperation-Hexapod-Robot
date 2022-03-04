from threading import Timer, Thread, Event

ARTICULATION_NUMBER = 18


class PlannerTimer(Thread):
    """
    Timer in order to check if there are steps left to satisfy 
    the position commands of the robot.

    Args:
        Thread ([class]): [Thread class]
    """

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
                self.gl.planner_steps = self.gl.planner_steps - 1
                self.gl.walking_input(self.gl.planner_angle)
