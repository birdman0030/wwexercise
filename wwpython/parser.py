#!/usr/bin/env python

from configuration import ROOT_DIR
import os.path


class Parser:
    def __init__(self):
        self.dn = os.path.join(ROOT_DIR, "wwpython", "data")

    def doesFileExist(self, filename: str):
        """
        Verifies if a file exists and throws an IOError exception if not found.

        :param filename: name of file contained in the data directory
        """

        path = os.path.join(self.dn, filename)
        if os.path.isfile(path):
            print("File exists")
        else:
            raise IOError(f"{path} does not exist")

    def parseFile(self, filename: str):
        """
        Parses a text file given the following format:
            <key> - <val1>, <val2),...

        :param filename: name of file contained in the data directory.
        :return d: dictionary of parsed text file.
        """
        d = {}
        path = os.path.join(self.dn, filename)
        with open(path) as f:
            for line in f:
                (key, val) = line.strip().split('-')
                vals = val.split(',')
                d[str(key)] = vals
        return d

    def printResults(self, d: dict):
        """
        Print the content of a dictionary in the following format:
            key
            val1
            val2
            ...

        :param d: a dictionary object.
        """
        for key, val in d.items():
            print(key)
            for v in val:
                print(v.strip())


if __name__ == "__main__":
    filename = "sample_data.txt"
    parse = Parser()
    parse.doesFileExist(filename)
    results = parse.parseFile(filename)
    parse.printResults(results)
