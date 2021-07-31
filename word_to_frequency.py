import os
import csv


# function that will return frequency for a search keyword from a file 'unigram_freq.csv' (row count: 333334)
def get_freq(word):

    # To locate the file
    loc_file_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(loc_file_path, 'unigram_freq.csv')

    # reading file to search frequency for the word
    with open(filename, 'r') as csv_file:
        data_reader = csv.reader(csv_file)
        for row in data_reader:
            if row[0] == word:
                return row[1]
    return "Keyword Not Found!"
