"""
Converter script.
Put your txt-files in `input_files` dir and run the script.
CSV-files will be generated in `output_files`.
"""

import csv
import itertools
import os


def main():
    input_dir = 'input_files/'
    for file in os.listdir(input_dir):
        convert_file(input_dir, file)


def convert_file(input_dir, file):
    with open(input_dir + file, 'r') as in_file:
        lines = in_file.read().splitlines()
        stripped = [line.replace(",", " ").split() for line in lines]
        grouped = itertools.izip(*[stripped]*1)
        with open('output_files/' + os.path.splitext(file)[0] + '.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            for group in grouped:
                writer.writerows(group)


if __name__ == '__main__':
    main()
