# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data

    def extract_header(self):
        self.header = self.data[0]


import csv
f = open("nfl.csv", 'r')
nfl_data = csv.reader(f)
dataset_data = list(nfl_data)


nfl_dataset = Dataset(dataset_data)
nfl_header = nfl_dataset.extract_header()
print(nfl_dataset.extract_header())


