#!/usr/bin/python3
"""
CSV to JSON module
"""
import csv, json


def convert_csv_to_json(csv_filename):
    csv_list = []
    try:
        with open(csv_filename, encoding="utf-8") as csvf:
            csv_reader = csv.DictReader(csvf)
            for row in csv_reader:
                csv_list.append(row)
        with open("data.json", "w", encoding="utf-8") as jsonf:
            json.dump(csv_list, jsonf, indent=4)
    except FileNotFoundError:
        return False
    return True
