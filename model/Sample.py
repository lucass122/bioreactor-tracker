class Sample:
    # name: name of sample; taxa: list with all taxa that belong to sample
    def __init__(self, name, taxa, taxon_names, taxon_abundances):
        self.name = name
        self.taxa = taxa
        # name and abundances lists are stored redundantly for easier access and plotting)
        self.taxon_names = taxon_names
        self.taxon_abundances = taxon_abundances

    def add_taxon(self, taxon):
        self.taxa.append(taxon)

    def add_taxon_names(self, taxon_names):
        self.taxon_names = taxon_names

    def add_taxon_abundances(self, taxon_abundances):
        self.taxon_abundances = taxon_abundances
