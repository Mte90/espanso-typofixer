#!/usr/bin/env python3
import argparse
import os.path
import csv
from SyntaxAutoFix.utils import open_typo_file, save_typo_data

# Parse argument
parser = argparse.ArgumentParser(description='add new terms!')

parser.add_argument('-file', dest="file", type=str, required=True)
parser.add_argument('-lang', dest="lang", type=str, required=True)
parser.add_argument('-opposite', dest="opposite", type=bool, required=False)
args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(script_path, '../words/' + args.lang + '.json')

typo_data = open_typo_file(script_path)

with open(args.file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    exact = 0
    wrong = 1
    if args.opposite:
        exact = 1
        wrong = 0
    for row in csv_reader:
        if row[exact] in typo_data:
            typo_data[row[exact]].append(row[wrong])
        else:
            typo_data[row[exact]] = [row[wrong]]

save_typo_data(script_path, typo_data)
