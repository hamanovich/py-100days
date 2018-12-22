import os
import csv
import collections
from typing import List

Record = collections.namedtuple(
    'Record', 'year,month,date_of_month,day_of_week,births'
)

DIRECTORY = os.path.join(os.path.dirname(__file__), '..', 'tmp')
FILENAME = os.path.join(DIRECTORY, 'US_births_2000-2014_SSA.csv')


def load_file(filename=FILENAME) -> List[Record]:
    data = []
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        data.clear()
        for row in reader:
            record = parse_row(row)
            data.append(record)

    return data


def parse_row(row):
    row['year'] = int(row['year'])
    row['month'] = int(row['month'])
    row['date_of_month'] = int(row['date_of_month'])
    row['day_of_week'] = int(row['day_of_week'])
    row['births'] = int(row['births'])

    return Record(**row)
