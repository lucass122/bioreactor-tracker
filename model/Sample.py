class Sample:
    # name: name of sample; taxa: list with all taxa that belong to sample
    def __init__(self, name, taxa):
        self.name = name
        self.taxa = taxa

    def add_taxon(self, taxon):
        self.taxa.append(taxon)
