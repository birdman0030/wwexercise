#!/usr/bin/env python

from random import randint


def randomNumGen():
    """
    Generates a list of 500 random numbers between 0-1000.

    :return generated: a list of integers.
    """
    generated = [randint(0, 1000) for i in range(500)]
    return generated


def findNumPosition(nums, val):
    """
    Converts a list of integers to a set and returns the nth value.

    :param nums: a list of integers.
    :param val: a nth value to find in a list of integers.
    """
    gen_sort = set(nums)
    return sorted(gen_sort)[val]


if __name__ == "__main__":
    container = randomNumGen()
    print(container)
    print(findNumPosition(container, 10))
