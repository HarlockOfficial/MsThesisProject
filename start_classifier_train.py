import sys

import EEGClassificator

if __name__ == '__main__':
    path_to_network = sys.argv[1] if len(sys.argv) > 1 else None
    EEGClassificator.PersonalModel.main(path_to_network)
