'''
client.py - run client TCP from stdin to server

    Args in stdin:
        server_ip (str): the server's ip
        server_port (int): the server's port
        data (str): message to send

'''

import argparse
import sys
from connection import Connection
###########################################################
####################### YOUR CODE #########################
###########################################################
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
        with Connection.connect(args.server_ip, args.server_port) as conn:
            conn.send_message(args_data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
