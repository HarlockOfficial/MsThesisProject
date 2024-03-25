import sys

import EEGClassificator.Tester

if __name__ == '__main__':
    path_to_network = sys.argv[1]
    EEGClassificator.Tester.main(path_to_network)
