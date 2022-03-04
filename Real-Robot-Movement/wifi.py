import socket

""" HOST = '127.0.0.1'
HOST = '192.168.1.39' """
HOST = "191.82.52.80"
PORT = 8080


class WifiClient:
    """
    Class to manage the wifi communication with the server
    """

    def __init__(self, gl):
        self.gl = gl
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # s.sendall(b'Hello, world')
            while 1:

                try:
                    s.sendall(b"Checking connection")
                    data = s.recv(22)
                    self.command_interpreter(data.decode("utf-8"))
                except:
                    print("Reconnecting")
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        s.connect((HOST, PORT))
                    except:
                        print("Connection not posible")

    def command_interpreter(self, data):
        print(data)
        if data[1] == "J":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = int(data[4:end_index])
            self.gl.set_joint_trajectory([value], [1], int(data[2]), int(data[3]))

        if data[1] == "P":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            values = data[2 : end_index - 1].split(",")
            for i in range(6):
                self.gl.platform_variables[i] = int(values[i])
            self.gl.platform_movement()

        if data[1] == "W":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.walk(value)

        if data[1] == "R":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.rotation(value)

        if data[1] == "C":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            values = data[2 : end_index - 1].split(",")

            print("#######################")
            print(int(values[0]))
            print(int(values[1]))
            print(self.gl.step_distance)
            self.gl.set_robot_movement(int(values[0]), int(values[1]))

        if data[1] == "V":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = float(data[2 : end_index - 1])
            print(value)
            self.gl.set_velocity(value)

        if data[1] == "D":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.set_step_distance(value)

        if data[1] == "H":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.set_step_height(value)

        if data[1] == "S":
            end_index = 0
            for i in range(len(data)):
                if data[i] == "=":
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.set_rotation_step(value)
