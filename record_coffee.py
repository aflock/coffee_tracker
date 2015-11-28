"""Record Coffee

Usage:
    record_coffee.py [--format=<fmt>] [--mg=<mg>]

Options:
  --format=<fmt> What beverage [default: 'coffee'].
  --mg=<mg>      How many milligrams of caffeine [default: 80]

"""

import csv
import subprocess
import IPython
import os
import time
import json
from docopt import docopt

# Constants
FILENAME = "coffeelog.csv"
FIELDS = ['mg', 'date', 'format']
DEFAULT_MG = 80
DEFAULT_FMT = 'coffee'

def main(arguments):
    if '--format' in arguments and arguments['--format']:
        fmt = arguments['--format']
    else:
        fmt = DEFAULT_FMT

    if '--mg' in arguments and arguments['--mg']:
        mg = arguments['--mg']
    else:
        mg = DEFAULT_MG

    record_coffee(fmt, mg)
    # upload()

def record_coffee(fmt, mg):
    print("record ", fmt, mg)
    with open('coffeelog.json', 'r') as json_data:
        data = json.load(json_data)
    with open('coffeelog.json', 'w+') as json_data:
        data['data'].append({"mg":int(mg), "date":time.time(), "format":fmt})
        json.dump(data, json_data)


if __name__ == '__main__':
    arguments = docopt(__doc__)
    main(arguments)
