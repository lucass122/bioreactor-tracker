import os

from parser.ParserInterface import ParserInterface


# file has the following format
# accession	accession.version	taxid	gi
# P26567	P26567.2	4577	1168978

class Taxid2NameParser(ParserInterface):
    def __init__(self, file_path):
        self.file_path = file_path
        self.taxid_to_name_dict = {}

    def load_data_source(self):
        self.taxid_to_name_dict = {}
        print(f"Loading NCBI Map at {self.file_path}...")
        if os.path.isfile(self.file_path):
            with open(self.file_path) as f:
                for line in f:
                    # convert to int after parsing for dict to work properly
                    taxid = int(line.split('\t')[0].rstrip())
                    name = line.split('\t')[1].rstrip()
                    self.taxid_to_name_dict[taxid] = name

        else:
            raise FileNotFoundError(f"File {self.file_path} not found. Please check the file path.")

    def extract_data(self, taxid, name):
        pass
