'''
    server.py - run server TCP from stdin to server
    Args when executing script:
        server_ip (str): the server's ip
        server_port (int): the server's port

'''
import argparse
import sys
import threading
import listener 
from connection import Connection


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


def handle_client(connection: Connection):
    with connection:
        print(connection.receive_message())



def main():
    '''Implementation of CLI and running server.'''
    args = get_args()

    try:
        with listener.Listener(args.server_ip, args.server_port) as server:
            while True:
                conn = server.accept()
                t = threading.Thread(target=handle_client, args=(conn,))
                t.start()

    except Exception as error:
    
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
