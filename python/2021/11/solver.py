import argparse
from copy import deepcopy

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()
if args.test:
    tab = [ [5,4,8,3,1,4,3,2,2,3],
            [2,7,4,5,8,5,4,7,1,1],
            [5,2,6,4,5,5,6,1,7,3],
            [6,1,4,1,3,3,6,1,4,6],
            [6,3,5,7,3,8,5,4,7,8],
            [4,1,6,7,5,2,4,6,4,5],
            [2,1,7,6,8,4,1,7,2,1],
            [6,8,8,2,8,8,1,1,3,4],
            [4,8,4,6,8,4,8,5,5,4],
            [5,2,8,3,7,5,1,5,2,6]]
    # tab = [
    #     [1,1,1,1,1],
    #     [1,9,9,9,1],
    #     [1,9,1,9,1],
    #     [1,9,9,9,1],
    #     [1,1,1,1,1]]
else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab.append([int(i) for i in line.strip("\n")])             
    file.close()


def get_neighbors(tab, i, j, diagonal_allowed=True):
    """Given a two dimensionnal array, return a list of tuple describing the neighbors of the coordinates x and y
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

part_two_tab = deepcopy(tab)
nb_flashes = 0
nb_steps = 100
for step in range(nb_steps):
    flashes = [] # List of octopus that will flahs
    flashed = [] # list of octopus that have flashed
    # first update
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j] += 1
            if tab[i][j] == 10:
                flashes.append((i,j))
                nb_flashes += 1
                tab[i][j] = 0
                flashed.append((i,j))
    # Updating flashes while there is flash
    while flashes:
        tmp_flash = flashes.copy()
        for flash in tmp_flash:
            flashes.remove(flash)
            flashed.append(flash)
            neighbors = get_neighbors(tab, flash[0], flash[1])
            for neighbor in neighbors:
                if neighbor not in flashed: # Update only if the octopus didn't flashed
                    tab[neighbor[0]][neighbor[1]] += 1
                    if tab[neighbor[0]][neighbor[1]] == 10:
                        flashes.append(neighbor)
                        flashed.append(neighbor)
                        nb_flashes += 1
                        tab[neighbor[0]][neighbor[1]] = 0
    # print(f"Step n°{step}")
    # for i in tab:
    #     print(i)
print("Solution part one : ", nb_flashes)

# PART TWO
all_flashed = False
step = 0
while not all_flashed:
    flashes = [] # List of octopus that will flahs
    flashed = [] # list of octopus that have flashed
    # first update
    for i in range(len(part_two_tab)):
        for j in range(len(part_two_tab[i])):
            part_two_tab[i][j] += 1
            if part_two_tab[i][j] == 10:
                flashes.append((i,j))
                nb_flashes += 1
                part_two_tab[i][j] = 0
                flashed.append((i,j))
    # Updating flashes while there is flash
    while flashes:
        tmp_flash = flashes.copy()
        for flash in tmp_flash:
            flashes.remove(flash)
            flashed.append(flash)
            neighbors = get_neighbors(part_two_tab, flash[0], flash[1])
            for neighbor in neighbors:
                if neighbor not in flashed: # Update only if the octopus didn't flashed
                    part_two_tab[neighbor[0]][neighbor[1]] += 1
                    if part_two_tab[neighbor[0]][neighbor[1]] == 10:
                        flashes.append(neighbor)
                        flashed.append(neighbor)
                        part_two_tab[neighbor[0]][neighbor[1]] = 0
    all_flashed = (len(set(flashed)) == len(part_two_tab)*len(part_two_tab[0]))
    step += 1

print(f"Step n°{step}")
for i in part_two_tab:
    print(i)
print("Solution part 2 :", step)