from datetime import date


# simple class representing the structure of a project. has project name, sample list, description and a date


class Project:

    def __init__(self, name, samples, description):
        self.name = name
        self.samples = samples
        self.description = description
        self.date = date.today()
