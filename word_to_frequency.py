import os
import csv


def get_freq(word):

    # To locate file
    loc_file_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(loc_file_path, 'unigram_freq.csv')
    with open(filename, 'r') as csv_file:
        data_reader = csv.reader(csv_file)
        for row in data_reader:
            if row[0] == word:
                return row[1]
    return "Keyword Not Found!"
