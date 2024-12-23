"""
This file regroup functions often used for AoC problems.
"""

def get_neighbors(tab, i, j, diagonal_allowed=True):
    """Given a two dimensional array, return a list of tuple describing the neighbors of the coordinates x and y
    """
    neighbors = []
    if i+1 < len(tab):
        neighbors.append((i+1,j))
    if j+1 < len(tab[i]):
        neighbors.append((i, j+1))
    if j-1 >= 0:
        neighbors.append((i,j-1))
    if i-1 >= 0:
        neighbors.append((i-1, j))
    if diagonal_allowed:
        if i+1 < len(tab) and j+1 < len(tab[i]):
            neighbors.append((i+1, j+1))
        if i+1 < len(tab) and j-1 >= 0:
            neighbors.append((i+1, j-1))
        if i-1 >= 0 and j+1 < len(tab[i]):
            neighbors.append((i-1, j+1))
        if i-1 >= 0 and j-1 >= 0:
            neighbors.append((i-1, j-1))
    return neighbors