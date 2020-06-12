from tkinter import *
from functools import partial
import math

ARTICULATION_NUMBER = 18

class GUI():

    def __init__(self, window, gl):

        self.gl = gl
        self.lbl_joint_variables = []
        self.txt_joint_variables = []
        self.txt_platform_variables = []
        self.art_number = 18
        self.window = window
        self.show_interface()

    def action(self, joint_number):

        row, col = self.get_list_index(joint_number)
        value = self.txt_joint_variables[joint_number].get()
        #if float(value) < 180 and float(value) > 0:
        self.gl.set_joint_trajectory([float(value)], [1.0], row, col)

    def platform_action(self, plat_var_number):
        print(plat_var_number)
        value = self.txt_platform_variables[plat_var_number].get()
        print(value)

    def walking_action(self):
        value = self.txt_walk.get()
        print (float(value) * math.pi / 180)
        self.gl.walking_input(float(value) * math.pi / 180)

    def show_interface(self):

        row_number = 0

        lbl_platform = Label(self.window, text="Hexapod View", font=("Arial Bold", 15))
        lbl_platform.grid(column=0, row=row_number)
        row_number = row_number + 1

        row_number = self.create_platform_inputs(row_number)
        row_number = self.create_joints_titles(row_number)
        row_number = self.create_joints_inputs(row_number)
        row_number = self.create_walking_input(row_number)

    def create_walking_input(self, row_number):


        lbl_walk = Label(self.window, text="Walk", font=("Arial Bold", 15))
        lbl_walk.grid(sticky="W", column=0, row=row_number)
        row_number = row_number + 1

        btn = Button(self.window, text="Walk", command=self.walking_action)
        btn.grid(column=0, row=row_number)



        self.txt_walk = Entry(self.window, width=10)
        self.txt_walk.grid(column=1, row=row_number)

        row_number = row_number + 1
        return row_number

    def create_platform_inputs(self, row_number):
        lbl_platform = Label(self.window, text="Platform", font=("Arial Bold", 15))
        lbl_platform.grid(sticky="W", column=0, row=row_number)
        row_number = row_number + 1

        lbl_x = Label(self.window, text="X", font=("Arial", 12))
        lbl_x.grid(column=1, row=row_number)

        lbl_y = Label(self.window, text="Y", font=("Arial", 12))
        lbl_y.grid(column=3, row=row_number)

        lbl_z = Label(self.window, text="Z", font=("Arial", 12))
        lbl_z.grid(column=5, row=row_number)
        row_number = row_number + 1

        counter_column = 1
        for i in range(3):

            self.txt_platform_variables.append(Entry(self.window, width=10))
            self.txt_platform_variables[i].grid(column=counter_column, row=row_number)
            counter_column = counter_column + 1

            btn = Button(self.window, text="Update", command=partial(self.platform_action, i))
            btn.grid(column=counter_column, row=row_number)
            counter_column = counter_column + 1
        row_number = row_number + 1

        lbl_x = Label(self.window, text="Roll", font=("Arial", 12))
        lbl_x.grid(column=1, row=row_number)

        lbl_y = Label(self.window, text="Pitch", font=("Arial", 12))
        lbl_y.grid(column=3, row=row_number)

        lbl_z = Label(self.window, text="Yaw", font=("Arial", 12))
        lbl_z.grid(column=5, row=row_number)
        row_number = row_number + 1

        
        counter_column = 1
        for i in range(3):

            self.txt_platform_variables.append(Entry(self.window, width=10))
            self.txt_platform_variables[i + 3].grid(column=counter_column, row=row_number)
            counter_column = counter_column + 1

            btn = Button(self.window, text="Update", command=partial(self.platform_action, i + 3))
            btn.grid(column=counter_column, row=row_number)
            counter_column = counter_column + 1
        row_number = row_number + 1




        return row_number




    def create_joints_titles(self, row_number):
        lbl_joints = Label(self.window, text="Joints", font=("Arial Bold", 15))
        lbl_joints.grid(sticky="W", column=0, row=row_number)
        row_number = row_number + 1


        lbl_coxa = Label(self.window, text="Coxa", font=("Arial", 12))
        lbl_coxa.grid(column=1, row=row_number)

        lbl_femur = Label(self.window, text="Femur", font=("Arial", 12))
        lbl_femur.grid(column=3, row=row_number)

        lbl_tibia = Label(self.window, text="Tibia", font=("Arial", 12))
        lbl_tibia.grid(column=5, row=row_number)
        row_number = row_number + 1
        return row_number


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

    def create_joints_inputs(self, row_number):

        counter_row = 0
        counter_column = 1

        for i in range(self.art_number):
            self.txt_joint_variables.append(Entry(self.window, width=10))
            self.txt_joint_variables[i].grid(column=counter_column, row=row_number+counter_row)
            counter_column = counter_column + 1

            btn = Button(self.window, text="Update", command=partial(self.action, i))
            btn.grid(column=counter_column, row=row_number+counter_row)
            counter_column = counter_column + 1

            if counter_column > 6:
                counter_column = 1
                counter_row = counter_row + 1

                self.lbl_joint_variables.append(Label(self.window, text=str(counter_row), font=("Arial", 12)))
                self.lbl_joint_variables[counter_row - 1].grid(column=0, row=row_number + counter_row -1)

        return row_number + counter_row

def runGUI(gl):
    window = Tk()
    window.title("Hexapod View")
    GUI(window, gl)
    window.geometry('600x500')
    window.mainloop()
