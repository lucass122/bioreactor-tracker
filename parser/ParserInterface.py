from abc import ABC, abstractmethod


class ParserInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load_data_source(self, path):
        pass

    @abstractmethod
    def extract_data(self):
        pass
