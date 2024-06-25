import sys

import EEGClassificator.TimeTester

if __name__ == '__main__':
    path_to_network = sys.argv[1:]
    EEGClassificator.TimeTester.main(path_to_network)
