import sys
import VirtualController

def main(path_to_generators, path_to_classificator, websocket_server_url):
    VirtualController.main(path_to_generators, path_to_classificator, websocket_server_url)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: start_virtual_controller.py <path_to_generators> <path_to_classificator> <websocket_server_url>")
        sys.exit(1)

    path_to_generators = sys.argv[1]
    path_to_classificator = sys.argv[2]
    websocket_server_url = sys.argv[3]
    main(path_to_generators, path_to_classificator, websocket_server_url)
