#!/usr/bin/env python

from configuration import ROOT_DIR

import os.path
import logging


class Parser:
    def __init__(self, path: str):
        self.path = os.path.join(ROOT_DIR, path)
        self.logger = logging.getLogger("parser")

    def doesFileExist(self):
        """
        Verifies if a file exists and throws an IOError exception if not found.
        """

        if os.path.isfile(self.path):
            return True
        else:
            raise IOError(f"{self.path} does not exist")

    def parseFile(self):
        """
        Parses a text file given the following format:
            <key> - <val1>, <val2),...

        :return d: dictionary of parsed text file.
        """
        d = {}
        with open(self.path) as f:
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
            self.logger.info(key)
            for v in val:
                self.logger.info(v.strip())
