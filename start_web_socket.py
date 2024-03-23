import sys
import subprocess
from datetime import datetime


def main(*args):
    if len(args) == 0:
        host = '127.0.0.1'
        port = 8000
    elif len(args) == 1:
        host = args[0]
        port = 8000
    elif len(args) == 2:
        host = args[0]
        port = args[1]
    else:
        print('Usage: python3.11 start_web_socket.py <host> <port>')
        exit(1)

    t = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    log = open(f'WebsocketServer/logs/log_{t}.log', 'w')
    err = open(f'WebsocketServer/logs/err_{t}.log', 'w')
    process = subprocess.run(['../.venv/bin/uvicorn', 'main:app', '--host', host, '--port', str(port)], stdout=log, stderr=err, cwd='WebsocketServer')
    log.close()
    err.close()
    print('WebSocket started')


if __name__ == '__main__':
    main(sys.argv[1:])