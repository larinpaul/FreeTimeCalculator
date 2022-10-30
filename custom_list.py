""" This module adds the functionality
of ignoring the conflicts of those elements of a list
that are already removed from the list,
by passing the elements instead of throwing the ValueError
"""
from multiprocessing.sharedctypes import Value

class CustomList(list):
    def remove_if_exist(self, v):
        try:
            self.remove(v)
        except ValueError:
            pass
