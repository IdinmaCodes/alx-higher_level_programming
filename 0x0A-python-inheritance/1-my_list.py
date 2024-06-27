#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from
the built-in list class and adds a method to print the
list elements in sorted order.
"""


class MyList(list):
    """Class that extends the functionality of the built-in list class."""
    def print_sorted(self):
        """Prints the list elements in sorted order."""
        print(sorted(self))
