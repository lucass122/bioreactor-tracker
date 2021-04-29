# This class represents a pie plot of one sample visualizing abundances
# @param sample: sample used for plotting
import plotly.express as px

class AbundancePie:

    def __init__(self, sample):
        self.sample = sample

    def plot_pie(self):
        fig = px.pie(self.sample.taxon_abundances, values=self.sample.taxon_abundances, names=self.sample.taxon_names,
                     title=f"Bacterial abundances of sample {self.sample.name} as a pie chart")
        fig.show()

    # function to filter zero values from abundance list and removing the names accordingly
    # if it's called new filtered lists are created and the original lists in the sample object are replaced by them

    # def filter_zero(self):
    #     abundances_filtered = []
    #     names_filtered = []
    #     for i, abundance in enumerate(self.sample.taxon_abundances):
    #         if abundance != 0:
    #             abundances_filtered.append(abundance)
    #             names_filtered.append(self.sample.taxon_names[i])
    #     self.sample.taxon_abundances = abundances_filtered
    #     self.sample.taxon_names = names_filtered
