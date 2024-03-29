import os
import sys
import csv
from itertools import islice

from network import download_gzip


DATA_URL = "http://cdsarc.u-strasbg.fr/viz-bin/nph-Cat/txt.gz?I/239/hip_main.dat"
DATA_FOLDER_NAME = "../data"
FULL_DATA_FILE_NAME = f"{DATA_FOLDER_NAME}/I_239_hip_main.dat"
CSV_DATA_FILE_NAME = f"{DATA_FOLDER_NAME}/hip_main.csv"
DATA_START_INDEX = 12
DATA_END_INDEX = 118230

dirname = os.path.dirname(__file__)
data_folder_path = os.path.join(dirname, DATA_FOLDER_NAME)
full_data_path = os.path.join(dirname, FULL_DATA_FILE_NAME)
csv_data_path = os.path.join(dirname, CSV_DATA_FILE_NAME)


def download_and_save():
    if not os.path.exists(data_folder_path):
        os.makedirs(data_folder_path)

    parseable_data = download_gzip(DATA_URL)
    with open(full_data_path, 'wb') as f:
        for chunk in parseable_data:
            f.write(chunk)


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
                should_ignore_warning = '--iw' in sys.argv
                if not should_ignore_warning:
                    print(f"Error on line {line_num+1} - missing some values.")


download_and_save()
data_to_csv()
print("Done.")
