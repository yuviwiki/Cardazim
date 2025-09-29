import socket
import struct

class Connection:


    def __init__(self, connection: socket.socket):
        self.connection = connection 


    def __repr__(self):
        return f'<Connection from \
{self.connection.getsockname()[0]}:{self.connection.getsockname()[1]} \
to {self.connection.getpeername()[0]}:{self.connection.getpeername()[1]}>'


    @classmethod
    def connect(cls, server_ip: str, server_port: int):

        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((server_ip,server_port))
        return cls(client)


    def send_message(self,data: bytes):
        '''
        Send data to server in address (server_ip, server_port).
        '''
        size = len(data)
        size_bytes = struct.pack("<I",size)
        #creating the client socket
        self.connection.sendall(size_bytes + data)


    def receive_message(self):
        try:
            size_byte = self.connection.recv(4)
            size = struct.unpack("<I",size_byte)[0]
            message = self.connection.recv(size).decode('utf-8')
            return message
        except socket.error as e:
            print(f"ERROR: {e}")
            return None



    def close(self):
        try:
            self.connection.close()
        except Exception as e:
            print(f"ERROR: {e}")


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return False        
