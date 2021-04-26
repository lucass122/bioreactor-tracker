# This is a sample Python script.
from model.Project import Project
from model.Sample import Sample
from model.User import User
from parser.MairaParser import MairaParser
from plot.AbundancePie import AbundancePie

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = MairaParser()
    p.load_data_source("/Users/timolucas/PycharmProjects/phd-project/resources/simulated_tree")
    p.extract_data()

    sample1 = Sample("Simulated test sample", p.taxa, p.names, p.abundances)
    project1 = Project("Caner's simulated test project", sample1,
                       "This project contains only simulated data for testing "
                       "purposes.")
    user1 = User("Timo", project1)

    print(f"User: {user1.name}")
    print(f"Sample: {sample1.name}")
    print(f"Project: {project1.name} created on {project1.date}. Project description: {project1.description}")
    #     try plotting stuff
    pie_plotter = AbundancePie(sample1)
    pie_plotter.filter_zero()
    pie_plotter.plot_pie()
