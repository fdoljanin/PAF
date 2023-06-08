import os
import csv
from datetime import datetime, timezone, timedelta

from classes import *
from criteria import *
from request_helper import *


DATA_FILE_NAME = "../data/hip_main.csv"

dirname = os.path.dirname(__file__)
data_path = os.path.join(dirname, DATA_FILE_NAME)


def count_stars(location, time):
    check_is_visible = get_star_checker(location, time)
    visible_stars_count = 0

    with open(data_path, 'r') as data_file:
        csv_reader = csv.reader(data_file, delimiter=',')
        for line in csv_reader:
            star = Star(*line)
            if check_is_visible(star):
                visible_stars_count += 1

    return visible_stars_count


def main():
    observed_location_name = input("Enter location name:\t")
    current_location = get_location_from_name(observed_location_name)
    current_time = datetime.now(timezone.utc)

    visible_stars_count = count_stars(current_location, current_time)
    print(f"Visible stars: {visible_stars_count}")

main()