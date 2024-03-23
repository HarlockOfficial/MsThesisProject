import datetime
import subprocess
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python3.11 main.py <action_to_start>')
        exit(1)
    action = sys.argv[1]
    if action.lower().strip() == 'augment':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('DatasetAugmentation/logs/log_' + t + '.log', 'w')
        err = open('DatasetAugmentation/logs/err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_augmentation_train.py'], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Augmentation finished')
    elif action.lower().strip() == 'train':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_train.py'], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Training finished')
    else:
        print('Usage: python3.11 main.py <augment|train>')
        exit(1)
