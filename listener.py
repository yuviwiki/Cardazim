import socket
import connection

class Listener:

    def __init__(self, host: str, port: int, backlog: int = 1000):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))


    def __repr__(self):
        return f'<Listener(port={self.port}, host="{self.host}", backlog={self.backlog})>'


    def start(self):
        self.server_socket.listen(self.backlog)
        print(f'Listening on {self.host}:{self.port}...')


    def stop(self):
        self.server_socket.close()
        print('Listener stopped.')


    def accept(self):
        client_socket, client_address = self.server_socket.accept()
        print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
        return connection.Connection(client_socket)


    def __enter__(self):
        self.start()
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
        return False