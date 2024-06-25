import sys

import EEGClassificator.ClassificationAccuracyTesterGAN

if __name__ == '__main__':
    gan_folder = sys.argv[1]
    path_to_network = sys.argv[2:]
    EEGClassificator.ClassificationAccuracyTesterGAN.main(gan_folder, path_to_network)
