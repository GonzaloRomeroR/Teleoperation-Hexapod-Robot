import socket
HOST = '127.0.0.1'
PORT = 8080


class WifiClient():

    def __init__(self, gl):
        self.gl = gl
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            #s.sendall(b'Hello, world')
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
        
        if data[1] == 'J':
            end_index = 0
            for i in range(len(data)):
                if data[i] == '=':
                    end_index = i
                    break
            value = int(data[4:end_index])
            self.gl.set_joint_trajectory([value] ,[1],int(data[2]), int(data[3]))

        
        if data[1] == 'P':
            end_index = 0
            for i in range(len(data)):
                if data[i] == '=':
                    end_index = i
                    break
            values = data[2:end_index-1].split(",")
            for i in range(6):
                self.gl.platform_variables[i] = int(values[i])
            self.gl.platform_movement()


        if data[1] == 'W':
            end_index = 0
            for i in range(len(data)):
                if data[i] == '=':
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.walk(value)


        if data[1] == 'R':
            end_index = 0
            for i in range(len(data)):
                if data[i] == '=':
                    end_index = i
                    break
            value = int(data[2:end_index])
            print(value)
            self.gl.rotation(value)

        if data[1] == 'C':
            end_index = 0
            for i in range(len(data)):
                if data[i] == '=':
                    end_index = i
                    break
            values = data[2:end_index-1].split(",")
            print(values[0])
            print(values[1])
            #self.gl.move_to((int)values[0], (int)values[1])




