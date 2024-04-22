import sys
import EEGClassificator.PlotConfusionMatrix

if __name__ == '__main__':
    base_path = sys.argv[1]
    filename = sys.argv[2]
    EEGClassificator.PlotConfusionMatrix.main(base_path, filename)
