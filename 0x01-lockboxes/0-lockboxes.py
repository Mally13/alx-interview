#!/usr/bin/python3
"""
Contains the callUnlockAll method that determines if all
boxes can be opened
"""


def canUnlockAll(boxes):
    '''
    Determines if all boxes can be opened
    '''
    keysRequired = set(range(len(boxes)))
    keysFound = set([0])
    for box in boxes:
        for possibleKey in box:
            if possibleKey != 0 and possibleKey in keysRequired:
                keysFound.add(possibleKey)
                break
    soln = keysFound.issubset(
        keysRequired) and keysRequired.issubset(keysFound)
    return (soln)
