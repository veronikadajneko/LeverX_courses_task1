import json

from abc import ABC, abstractmethod


class Parser(ABC):
    """ Class for parses different files
    """
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def loader(self, file_name):
        pass


class ParserJSON(Parser):
    """ Class for parses json files
    """
    def loader(self, file_name):
        with open(file_name, 'r') as inf:
            text = json.load(inf)
            return text
