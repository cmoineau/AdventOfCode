import argparse
from copy import deepcopy

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()
if args.test:
    # tab = [ ("start","kj"),
    #         ("dc","end"),
    #         ("HN","start"),
    #         ("dc","start"),
    #         ("dc","HN"),
    #         ("LN","dc"),
    #         ("HN","end"),
    #         ("kj","sa"),
    #         ("kj","HN"),
    #         ("kj","dc")]
    tab = [ ("start","A"),
            ("start","b"),
            ("A","c"),
            ("A","b"),
            ("b","d"),
            ("A","end"),
            ("b","end")]
else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab.append(line.strip("\n").split("-"))             
    file.close()

def reachable_cells(cell):
    result = []
    for link in tab:
        i,j = link
        if cell == i:
            result.append(j)
        if cell == j:
            result.append(i)
    return result

def find_paths(current_cell, current_path):
    if current_cell == "end":
        return [current_path]
    if current_cell == "start" and current_path != []:
        return []
    paths = []
    r_cells = reachable_cells(current_cell)
    for r_cell in r_cells:
        if r_cell.isupper() or r_cell not in current_path :
            paths+= find_paths(r_cell, current_path + [r_cell])
    return paths

valid_paths = find_paths("start", [])
print(f"Solution part one : {len(valid_paths)}")

def find_paths_2(current_cell, current_path, twice):
    if current_cell == "end":
        return [current_path]
    if current_cell == "start" and current_path != []:
        return []
    paths = []
    r_cells = reachable_cells(current_cell)
    for r_cell in r_cells:
        if r_cell.isupper():
            paths+= find_paths_2(r_cell, current_path + [r_cell], twice)
        else:
            if (current_path.count(r_cell) < 1):
                paths+= find_paths_2(r_cell, current_path + [r_cell], twice)
            else:
                if not twice:
                    paths+= find_paths_2(r_cell, current_path + [r_cell], True)    
    return paths
    
valid_paths = find_paths_2("start", [], False)

print(f"Solution part two : {len(valid_paths)}")