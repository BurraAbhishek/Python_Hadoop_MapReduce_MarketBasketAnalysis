import json
import csv

# Convert a JSON file to CSV file
# This module is licensed under Public Domain.


def generate_csvdataset():
    """ Convert a JSON dataset to CSV dataset """

    with open("dataset/dataset.json", "r") as itemjson:
        items = json.load(itemjson)
        csvfile = open("dataset/csv_dataset.csv", "w")
        writer = csv.writer(csvfile)
        for i in range(0, len(items)):
            writer.writerow(items[i])
        csvfile.close()

generate_csvdataset()
