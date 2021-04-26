# simple class representing a taxon
# a taxon has an abundance, a phylogenetic level, a scientific name and a taxonomic id (ncbi id in case of MAIRA taxon)
class Taxon:
    def __init__(self, abundance, level):
        self.abundance = abundance
        self.level = level

    def set_name(self, name):
        self.name = name

    def set_abundance(self, abundance):
        self.abundance = abundance

    def set_taxid(self, taxid):
        self.taxid = taxid

    def set_attributes(self, attributes):
        self.attributes = attributes
       