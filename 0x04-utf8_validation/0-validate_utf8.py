#!/usr/bin/python3
"""
Contain a function that determines if a given data set
represents a valid UTF8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid utf8 encoding
    """
    if all(0 <= byte <= 127 for byte in data):
        return True
    else:
        return False
