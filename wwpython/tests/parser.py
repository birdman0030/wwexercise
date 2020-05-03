#!/usr/bin/env python

from ... import configuration
import os.path


def doesFileExist(path: str):
    """
    Verifies if a file exists and throws an IOError exception if not found.

    :param path: path to file relative to the project parent directory.
    """

    fn = os.path.join(os.path.dirname(ROOT_DIR, path))
    if os.path.isfile(fn):
        print("File exists")
    else:
        raise IOError(f"{path} does not exist")


def parseFile(path: str):
    """
    Verifies if a file exists and throws an IOError exception if not found.

    :param path: path to file relative to the project parent directory.
    :return d: dictionary of parsed text file.
    """
    d = {}
    with open(path) as f:
        for line in f:
            (key, val) = line.strip().split('-')
            vals = val.split(',')
            d[str(key)] = vals
    return d

def printResults(d: dict):
    """
    Print the content of a dictionary in the following format:
        key
        val1
        val2
        ...

    :param d: a dictionary object.
    """
    for key, val in d:
        print(d[key])
        for v in val:
            print(v)


if __name__ == "__main__":
    path = "sample_data.txt"
    doesFileExist(path)
    results = parseFile(path)
    printResults(results)
