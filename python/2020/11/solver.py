import argparse
from copy import deepcopy
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab=[
        ["L",".","L","L",".","L","L",".","L","L"],
        ["L","L","L","L","L","L","L",".","L","L"],
        ["L",".","L",".","L",".",".","L",".","."],
        ["L","L","L","L",".","L","L",".","L","L"],
        ["L",".","L","L",".","L","L",".","L","L"],
        ["L",".","L","L","L","L","L",".","L","L"],
        [".",".","L",".","L",".",".",".",".","."],
        ["L","L","L","L","L","L","L","L","L","L"],
        ["L",".","L","L","L","L","L","L",".","L"],
        ["L",".","L","L","L","L","L",".","L","L"]
    ]
else:
    tab = []
    file = open("./input", "r")

    for line in file:
        tab.append([i for i in line.strip("\n")])
    file.close()

# Part 1

def iterate(tab):
    new_tab = deepcopy(tab)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == "L":
                libre = True
                if i < len(tab)-1 and tab[i+1][j] == "#" :
                    libre = False
                if i < len(tab)-1 and j < len(tab[i+1])-1 and tab[i+1][j+1] == "#":
                    libre = False
                if i < len(tab)-1 and j > 0 and tab[i+1][j-1] == "#":
                    libre = False
                if i > 0 and tab[i-1][j] == "#":
                    libre = False
                if i > 0 and j < len(tab[i])-1 and tab[i-1][j+1] == "#" :
                    libre = False
                if i > 0 and j > 0 and tab[i-1][j-1] == "#":
                    libre = False
                if j < len(tab[i])-1 and  tab[i][j+1] == "#":
                    libre = False
                if j > 0 and tab[i][j-1] == "#":
                    libre = False

                if libre:
                    new_tab[i][j] = "#"

            elif tab[i][j] == "#":
                neighbor_nb = 0
                if i < len(tab)-1 and tab[i+1][j] == "#" :
                    neighbor_nb += 1
                if i < len(tab)-1 and j < len(tab[i+1])-1 and tab[i+1][j+1] == "#":
                    neighbor_nb += 1
                if i < len(tab)-1 and j > 0 and tab[i+1][j-1] == "#":
                    neighbor_nb += 1
                if i > 0 and tab[i-1][j] == "#":
                    neighbor_nb += 1
                if i > 0 and j < len(tab[i])-1 and tab[i-1][j+1] == "#" :
                    neighbor_nb += 1
                if i > 0 and j > 0 and tab[i-1][j-1] == "#":
                    neighbor_nb += 1
                if j < len(tab[i])-1 and  tab[i][j+1] == "#":
                    neighbor_nb += 1
                if j > 0 and tab[i][j-1] == "#":
                    neighbor_nb += 1

                if neighbor_nb >= 4:
                    new_tab[i][j] = "L"

            elif tab[i][j] == ".":
                pass
            else:
                raise RuntimeError(f"Unknown character : " + tab[i][j])
    return new_tab

def diff(t1,t2):
    for i in range(len(t1)):
        for j in range(len(t1[i])):
            if t1[i][j] != t2[i][j]:
                return True
    return False

old_tab = deepcopy(tab)
new_tab = deepcopy(tab)
not_equal = True
while not_equal:
    tmp = deepcopy(new_tab)
    new_tab = iterate(new_tab)
    old_tab = deepcopy(tmp)
    # for i in new_tab:
    #     print(i)
    not_equal = diff(old_tab, new_tab)

result = 0

for i in new_tab:
    for j in i:
        if j == "#":
            result += 1

print("Solution part 1 : ", result)



# Part 2

def direction_libre(tab, i, j, i_step, j_step):
    ni = i + i_step
    nj = j + j_step
    if not(0 <= ni < len(tab)):
        return True
    if not(0 <= nj < len(tab[ni])):
        return True
    
    if tab[ni][nj] == "#":
        return False
    elif tab[ni][nj] == "L":
        return True
    elif tab[ni][nj] == ".":
        return direction_libre(tab, ni, nj, i_step, j_step)
    else:
        raise RuntimeError("Invalid char !")

def new_iterate(tab):
    new_tab = deepcopy(tab)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == "L":
                libre = True
                libre = direction_libre(tab, i, j, 0, 1)
                
                libre = direction_libre(tab, i, j, 0, -1) and libre
                libre = direction_libre(tab, i, j, 1, 1) and libre
                libre = direction_libre(tab, i, j, 1, -1) and libre
                libre = direction_libre(tab, i, j, -1, 1) and libre
                libre = direction_libre(tab, i, j, -1, -1) and libre
                libre = direction_libre(tab, i, j, 1, 0) and libre
                libre = direction_libre(tab, i, j, -1, 0) and libre
                
                if libre:
                    new_tab[i][j] = "#"

            elif tab[i][j] == "#":
                neighbor_nb = 0
                if not direction_libre(tab, i, j, 0, 1):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, 0, -1):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, 1, 1):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, 1, -1):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, 1, 0):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, -1, -1):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, -1, 1):
                    neighbor_nb += 1
                if not direction_libre(tab, i, j, -1, 0):
                    neighbor_nb += 1

                if neighbor_nb >= 5:
                    new_tab[i][j] = "L"

            elif tab[i][j] == ".":
                pass
            else:
                raise RuntimeError("Unknown character : " + tab[i][j])
    return new_tab


old_tab = deepcopy(tab)
new_tab = deepcopy(tab)
not_equal = True
while not_equal:
    tmp = deepcopy(new_tab)
    new_tab = new_iterate(new_tab)
    old_tab = deepcopy(tmp)
    not_equal = diff(old_tab, new_tab)


result = 0

for i in new_tab:
    for j in i:
        if j == "#":
            result += 1

print("Solution part 2 : ", result)