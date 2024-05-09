#!/usr/bin/python3
"""
Contain a function that determines if a given data set
represents a valid UTF8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid utf8 encoding
    """
    if not all(0 <= byte <= 127 for byte in data):
        return False
    byte_data = bytes(data)
    try:
        byte_data.decode('utf-8')
        return True
    except UnicodeDecodeError as e:
        return False
    except (TypeError, ValueError):
        return False
