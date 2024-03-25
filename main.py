import datetime
import subprocess
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python3.11 main.py <action_to_start>')
        exit(1)
    action = sys.argv[1]
    if action.lower().strip() == 'data_augment_train':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('DatasetAugmentation/logs/log_' + t + '.log', 'w')
        err = open('DatasetAugmentation/logs/err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_augmentation_train.py'], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Augmentation finished')
    elif action.lower().strip() == 'data_augment_test':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('DatasetAugmentation/logs/test_log_' + t + '.log', 'w')
        err = open('DatasetAugmentation/logs/test_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_augmentation_test.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Augmentation test finished')
    elif action.lower().strip() == 'network_train':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_train.py'], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Training finished')
    elif action.lower().strip() == 'network_test':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/test_log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/test_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_test.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Testing finished')
    elif action.lower().strip() == 'start_controller':
        import start_virtual_controller
        start_virtual_controller.main(sys.argv[2], sys.argv[3], sys.argv[4])
    elif action.lower().strip() == 'ws':
        import start_web_socket
        start_web_socket.main(*sys.argv[2:])
    else:
        print('Usage: python3.11 main.py <data_augment_train|data_augment_test|network_train|network_test|start_controller|ws> <args>')
        exit(1)
