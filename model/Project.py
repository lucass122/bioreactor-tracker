from datetime import date


# simple class representing the structure of a project. has project name, sample, description and a date


class Project:

    def __init__(self, name, sample, description):
        self.name = name
        self.sample = sample
        self.description = description
        self.date = date.today()
