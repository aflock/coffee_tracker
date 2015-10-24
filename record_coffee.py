import csv
import subprocess
import os
import time
# Constants
FILENAME = "coffeelog.csv"
FIELDS = ['mg', 'date', 'format']
DEFAULT_MG = 80
DEFAULT_FMT = 'coffee'

def main():
    initial_run = FILENAME not in os.listdir('.')
    record_coffee(initial_run)
    upload()


def record_coffee(initial_run=False):
    with open(FILENAME, 'a') as f:
        writer = csv.DictWriter(f, fieldnames = FIELDS)
        if initial_run:
            writer.writeheader()
        writer.writerow({'mg': DEFAULT_MG, 'format': DEFAULT_FMT, 'date': time.time()})


def upload():
    subprocess.call('git -C ~/code/coffee add coffeelog.csv', shell=True)
    subprocess.call('git -C ~/code/coffee commit -m "Drank Cofee"', shell=True)
    subprocess.call('git -C ~/code/coffee  push', shell=True)

if __name__ == '__main__':
    main()
