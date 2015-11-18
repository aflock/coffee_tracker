import csv
import subprocess
import os
import time
import json
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
        writer.writerow({'mg': DEFAULT_MG, 'format': "coffee", 'date': time.time()})
    with open('coffeelog.json', 'r') as json_data:
        data = json.load(json_data)
    with open('coffeelog.json', 'w+') as json_data:
        data['data'].append({"mg":DEFAULT_MG, "date":time.time(), "format":"coffee"})
        json.dump(data, json_data)



def upload():
    subprocess.call('git add coffeelog.json', shell=True)
    subprocess.call('git commit -m "Drank Cofee"', shell=True)
    subprocess.call('git push', shell=True)

if __name__ == '__main__':
    main()
