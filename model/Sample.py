class Sample:
    # name: name of sample; taxa: list with all taxa that belong to sample
    """
    :cvar name = name of sample
    :cvar taxa = list with all Taxon objects that belong to the sample
    :cvar taxon_names = list with all taxon names
    :cvar taxon_abundances = list with abundances that belong to taxa
    TODO: Sample should not get taxon_names and taxon_abundances, but instead I should provide a method that computes it on demand!!!
    """

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
