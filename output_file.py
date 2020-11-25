import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

from abc import ABC, abstractmethod


class OutputFile(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def write(self, text):
        pass


class OutputJSON(OutputFile):
    """
    Class for output in JSON format
    """
    def write(self, text):
        """
        write information into JSON file
        """
        with open(self.file_name, "w") as wrt:
            json.dump(text, wrt, skipkeys=False, ensure_ascii=True,
                      check_circular=True, allow_nan=True,
                      cls=None, indent=4, separators=None, default=None, sort_keys=False)


class OutputXML(OutputFile):
    """
        Class for output in XML format
    """
    def write(self, text):
        """Write information into XML file"""
        with open(self.file_name, "w") as wrt:
            xml = dicttoxml(text, attr_type=False)
            pretty_printing = parseString(xml).toprettyxml()
            wrt.write(pretty_printing)
