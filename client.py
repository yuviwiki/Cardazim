'''
client.py - a 

'''

import argparse
import sys
import socket
import struct
###########################################################
####################### YOUR CODE #########################
###########################################################


def send_data(server_ip, server_port, data: bytes):
    '''
    Send data to server in address (server_ip, server_port).
    '''
    size = len(data)
    size_bytes = struct.pack("<I",size)
    #creating the client socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
        client.connect((server_ip,server_port))
        client.sendall(size_bytes + data)


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    parser.add_argument('data', type=str,
                        help='the data')
    return parser.parse_args()

def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        args_data =args.data.encode('utf-8')
        send_data(args.server_ip, args.server_port, args_data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
