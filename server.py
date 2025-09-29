import socket
import argparse
import sys
import struct
import threading

def get_args():
    '''
    Parse the command line arguments.    
    '''


    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    return parser.parse_args()


def run_server(ip,port):
    '''
    Run a TCP server that listens for incoming messages.
    '''
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((ip,port))
        server.listen()
        print(f"Server listening on {ip}:{port}")
        while True:
            client = server.accept()[0]
            t = threading.Thread(target=handle_client, args=(client,))
            t.start()


def handle_client(client):
    '''
    Handle client connection.
    '''
    with client:
        size_byte = client.recv(4)
        size = struct.unpack("<I",size_byte)[0]
        message = client.recv(size).decode('utf-8')
        print(f"Received data: {message}")
        client.close()
#run with python server.py <ip> <port> use 
def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
    except Exception as error:
        print(f'ERROR: {error}')
        return 1
if __name__ == '__main__':
    sys.exit(main())



#flow 
#1. get_args() -> parse the command line arguments
#2. main() -> call get_args() and run_server()
#3. run_server() -> create a TCP server, listen for incoming clients, for each client create new thread to handle client
#4. handle_client() -> receive data from client, print the data, close the client connection
#5. if __name__ == '__main__' -> call main() and exit with the return code

