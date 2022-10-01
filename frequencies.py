"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
import collections

def frequencies(items):

    # Your code goes here

    return collections.Counter(map(str, items))
