#!/usr/bin/python3
"""
pascal_triangle - Returns a list of integers representing the
Pascal's triangle of n.
"""

def pascal_triangle(n):
    """
    Returns a list of integers representing the 
    Pascal's triangle of n.
    """
    if n<=0:
        return []
    i = 0
    triangle = []
    while i < n:
        innerlist = []
        j = 0
        while j <= i:
            if j == 0 or j == i:
                innerlist.append(1)
            else:
                innerlist.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            j += 1
        i += 1
        triangle.append(innerlist)
    return triangle
