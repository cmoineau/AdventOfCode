import argparse
from termcolor import cprint # Import for a prettier print of boards to check if the win condition is good

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()


if args.test:
    tab = [
        [2,1,9,9,9,4,3,2,1,0],
        [3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],
        [8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]]

else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab.append([int(i) for i in line.strip("\n")])             
    file.close()
low_points = []
for i in range(len(tab)):
    for j in range(len(tab[i])):
        neigboors = []
        if i+1 < len(tab):
            neigboors.append(tab[i+1][j])
        if j+1 < len(tab[i]):
            neigboors.append(tab[i][j+1])
        if j-1 >= 0:
            neigboors.append(tab[i][j-1])
        if i-1 >= 0:
            neigboors.append(tab[i-1][j])
        is_a_low_point = True
        for neigboor in neigboors: 
            if tab[i][j] >= neigboor:
                is_a_low_point = False
        if is_a_low_point:
            low_points.append((i, j))

map = ""
for i in range(len(tab)):
    for j in range(len(tab[i])):
        if (i, j) in low_points:
            color = "red"                                                                                                                                                                                        
        else:
            color = "green"
        cprint(str(tab[i][j]), color, end="")
    cprint('')
print(f"Solution part ONE : {sum([tab[i][j]+1 for i, j in low_points])}")


def find_basin(tab, points, i, j):
    # Recursive function to find basin
    if i+1 < len(tab) and tab[i+1][j] != 9 and (i+1, j) not in points:
        points.append((i+1,j))
        points = find_basin(tab, points, i+1, j)
    if j+1 < len(tab[i]) and tab[i][j+1] != 9 and (i, j+1) not in points:
        points.append((i,j+1))
        points = find_basin(tab, points, i, j+1)    
    if j-1 >=0 and tab[i][j-1] != 9 and (i, j-1) not in points:
        points.append((i,j-1))
        points = find_basin(tab, points, i, j-1)
    if i-1 >=0 and tab[i-1][j] != 9 and (i-1, j) not in points:
        points.append((i-1,j))
        points = find_basin(tab, points, i-1, j)
    return points

basin_sizes = []
for low_point in low_points:
    new_basin = find_basin(tab, [low_point], low_point[0], low_point[1])
    # print('---DEBUG---')
    # map = ""
    # for i in range(len(tab)):
    #     for j in range(len(tab[i])):
    #         if (i, j) in new_basin:
    #             color = "red"                                                                                                                                                                                        
    #         else:
    #             color = "green"
    #         cprint(str(tab[i][j]), color, end="")
    #     cprint("")
    # print('-----------')

    basin_sizes.append(len(new_basin))

solution = 1
for size in sorted(basin_sizes, reverse=True)[:3]:
    print(size)
    solution *= size

print(f"Solution part TWO : {solution}")