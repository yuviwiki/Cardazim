import socket
import argparse
import sys
import struct
def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    return parser.parse_args()


def run_server(ip,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((ip,port))
        server.listen()
        while True:
            client = server.accept()[0]
            size_byte = client.recv(4)
            size = struct.unpack("<I",size_byte)[0]
            message = client.recv(size).decode('utf-8')
            print(f"Received data: {message}")
            client.close()


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
