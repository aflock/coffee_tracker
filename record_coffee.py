import csv
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


def record_coffee(initial_run=False):
    with open(FILENAME, 'a') as f:
        writer = csv.DictWriter(f, fieldnames = FIELDS)
        if initial_run:
            writer.writeheader()
        writer.writerow({'mg': DEFAULT_MG, 'format': DEFAULT_FMT, 'date': time.time()})

def upload():
    return

if __name__ == '__main__':
    main()
