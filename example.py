#!/usr/env/python

# Example Class for learning python unit testing
# Author: matt.j.bernhardt@gmail.com
# Version: 0.1

# Modules

# Variables

# Classes


class Example(object):
    """docstring for ClassName"""

    # Variables
    total = 0

    # Methods
    def __init__(self, total):
        super(Example, self).__init__()
        self.total = total

    def Increment(self, value):
        self.total += value
        return self.total

    def Decrement(self, value):
        self.total -= value
        return self.total


def create_example(total):
    foo = Example(total)
    return foo


if __name__ == "__main__":
    bar = create_example(0)
    print(str(bar.total))
    bar.Increment(1)
    print(str(bar.total))
