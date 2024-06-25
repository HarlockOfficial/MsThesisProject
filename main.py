import datetime
import os
import subprocess
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: python3.11 main.py <action_to_start>')
        exit(1)
    action = sys.argv[1]
    if action.lower().strip() == 'data_augment_train':
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        if not os.path.exists('DatasetAugmentation/logs'):
            os.makedirs('DatasetAugmentation/logs')
        log = open('DatasetAugmentation/logs/log_' + t + '.log', 'w')
        err = open('DatasetAugmentation/logs/err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_augmentation_train.py'], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Augmentation finished')
    elif action.lower().strip() == 'data_augment_train_stochastic':
        if not os.path.exists('DatasetAugmentation/logs'):
            os.makedirs('DatasetAugmentation/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('DatasetAugmentation/logs/stochastic_approach_log_' + t + '.log', 'w')
        err = open('DatasetAugmentation/logs/stochastic_approach_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_augmentation_train_stochastic.py'], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Augmentation finished')
    elif action.lower().strip() == 'data_augment_test':
        if not os.path.exists('DatasetAugmentation/logs'):
            os.makedirs('DatasetAugmentation/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('DatasetAugmentation/logs/test_log_' + t + '.log', 'w')
        err = open('DatasetAugmentation/logs/test_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_augmentation_test.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Augmentation test finished')
    elif action.lower().strip() == 'network_train':
        if not os.path.exists('EEGClassificator/logs'):
            os.makedirs('EEGClassificator/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_train.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Training finished')
    elif action.lower().strip() == 'network_test':
        if not os.path.exists('EEGClassificator/logs'):
            os.makedirs('EEGClassificator/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/test_log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/test_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_test.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Testing finished')
    elif action.lower().strip() == 'network_test_gan':
        if not os.path.exists('EEGClassificator/logs'):
            os.makedirs('EEGClassificator/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/test_log_gan_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/test_err_gan_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_test_gan.py', *sys.argv[2:]], stdout=log,
                                 stderr=err)
        log.close()
        err.close()
        print('Testing with GAN finished')
    elif action.lower().strip() == 'network_test_robustness':
        if not os.path.exists('EEGClassificator/logs'):
            os.makedirs('EEGClassificator/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/test_log_robustness_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/test_err_robustness_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_test_robustness.py', *sys.argv[2:]], stdout=log,
                                 stderr=err)
        log.close()
        err.close()
        print('Testing robustness finished')
    elif action.lower().strip() == 'network_classification_time_test':
        if not os.path.exists('EEGClassificator/logs'):
            os.makedirs('EEGClassificator/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/classification_time_log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/classification_time_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_time_test.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Testing classification time finished')
    elif action.lower().strip() == 'network_confusion_matrix_plot':
        if not os.path.exists('EEGClassificator/logs'):
            os.makedirs('EEGClassificator/logs')
        t = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        log = open('EEGClassificator/logs/confusion_matrix_log_' + t + '.log', 'w')
        err = open('EEGClassificator/logs/confusion_matrix_err_' + t + '.log', 'w')
        process = subprocess.run(['.venv/bin/python3.10', './start_classifier_confusion_matrix_plot.py', *sys.argv[2:]], stdout=log, stderr=err)
        log.close()
        err.close()
        print('Confusion matrix plot finished')
    elif action.lower().strip() == 'start_controller':
        import start_virtual_controller
        start_virtual_controller.main(sys.argv[2], sys.argv[3], sys.argv[4])
    elif action.lower().strip() == 'ws':
        import start_web_socket
        start_web_socket.main(*sys.argv[2:])
    else:
        print('Usage: python3.11 main.py <data_augment_train|data_augment_test|network_train|network_test|start_controller|ws> <args>')
        exit(1)
