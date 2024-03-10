import datetime
import subprocess

if __name__ == '__main__':
    t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    log = open('DatasetAugmentation/logs/log_' + t + '.log', 'w')
    err = open('DatasetAugmentation/logs/err_' + t + '.log', 'w')
    process = subprocess.run(['DatasetAugmentation/.venv/bin/python3.11', './start_train.py'], stdout=log, stderr=err)
    log.close()
    err.close()
