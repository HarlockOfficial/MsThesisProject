import sys

import EEGClassificator.RobustnessTest

if __name__ == '__main__':
    gan_folder = sys.argv[1]
    path_to_network = sys.argv[2:]
    EEGClassificator.RobustnessTest.main(gan_folder, path_to_network)
