import os
import csv

import requests
import gzip
import shutil

from itertools import islice

DATA_URL = "http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/txt.gz?I/239/hip_main.dat"
FULL_DATA_FILE_NAME = "../data/I_239_hip_main.txt"
CSV_DATA_FILE_NAME = "../data/hip_main.csv"
DATA_START_INDEX = 12
DATA_END_INDEX = 118230

dirname = os.path.dirname(__file__)
full_data_path = os.path.join(dirname, FULL_DATA_FILE_NAME)
csv_data_path = os.path.join(dirname, CSV_DATA_FILE_NAME)


def download_and_save():
    response = requests.get(DATA_URL)
    with open(full_data_path, 'wb') as data_file:
        data_file.write(response.content)


def line_to_data(line):
    data = line.split('|')
    v_mag = float(data[4])
    ra_deg, de_deg = map(float, data[7].split())

    return (v_mag, ra_deg, de_deg)


def data_to_csv():
    with open(full_data_path, 'r') as buff, open(csv_data_path, 'w', newline='') as csv_file:
        lines = islice(buff, DATA_START_INDEX, DATA_END_INDEX)
        csv_writer = csv.writer(csv_file, delimiter=',')

        for line_num, line in enumerate(lines, start=DATA_START_INDEX):
            try:
                new_data = line_to_data(line)
                csv_writer.writerow(new_data)
            except:
                print(f"Error on line {line_num+1} - missing some values.")


download_and_save()
# data_to_csv()
