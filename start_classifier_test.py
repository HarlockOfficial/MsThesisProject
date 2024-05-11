import sys

import EEGClassificator.ClassificationAccuracyTester

if __name__ == '__main__':
    path_to_network = sys.argv[1:]
    EEGClassificator.ClassificationAccuracyTester.main(path_to_network)
