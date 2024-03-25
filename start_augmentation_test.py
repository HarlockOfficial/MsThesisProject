import sys

import DatasetAugmentation.Specialized_EEG_Generators

if __name__ == '__main__':
    out_class = sys.argv[1]
    path_to_neural_network = sys.argv[2]
    DatasetAugmentation.Specialized_EEG_Generators.TestGenerators.Tester.main(out_class, path_to_neural_network)
