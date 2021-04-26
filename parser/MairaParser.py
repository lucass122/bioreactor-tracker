import os

import pandas as pd

from model.Taxon import Taxon
from parser.ParserInterface import ParserInterface
from parser.Taxid2NameParser import Taxid2NameParser


class MairaParser(ParserInterface):
    def __init__(self):
        self.data = pd.DataFrame
        self.taxa = {}
        taxid_to_name_path = "/Users/timolucas/PycharmProjects/phd-project/resources/ncbi_taxid_to_name"
        self.taxid_to_name_parser = Taxid2NameParser()
        self.taxid_to_name_parser.load_data_source(taxid_to_name_path)
        self.names = []
        self.abundances = []

    def load_data_source(self, file_path):
        if os.path.isfile(file_path):
            self.data = pd.read_csv(file_path, sep='\t')
        # a MAIRA summary file looks has the following structure
        # level | taxid | completeness | abundance

    def extract_data(self):
        for tax in self.data.iterrows():
            # taxon object with abundance and level (tax[1][0] and tax[1][3]
            cur_tax = tax[1][int(1)]
            # fill taxa dictionary by first dreating taxon objects with lwvel and abundance and then
            # adding taxid to it and then with taxid adding name to it using the taxid2name object from above
            abundance = tax[1][3]
            self.abundances.append(abundance)
            level = tax[1][0]
            self.taxa[cur_tax] = Taxon(abundance, level)
            taxid = cur_tax
            self.taxa[cur_tax].set_taxid(taxid)
            name = self.taxid_to_name_parser.taxid_to_name_dict[cur_tax]
            self.taxa[cur_tax].set_name(name)
            self.names.append(name)

            print(
                f"taxid: {self.taxa[tax[1][int(1)]].taxid}  name: {self.taxa[cur_tax].name}   abundance: {self.taxa[cur_tax].abundance}")

        # loop over all taxids in maira summary and create dictionary: key is taxid values are level, completeness and abundance
