import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()
if args.test:
    # TEST INPUT
    inputs = [[6,10],[0,14],[9,10],[0,3],[10,4],[4,11],[6,0],[6,12],[4,1],[0,13],[10,12],[3,4],[3,0],[8,4],[1,10],[2,14],[8,10],[9,0]]
    fold = [("y", 7), ("x", 5)]
else:
    # PARSING INPUT FILE
    file = open("./input", "r")
    header = True
    fold = []
    inputs = []
    for line in file:
        if line == "\n":
            header = False
        elif header:
            inputs.append([int(i) for i in line.split(",")])
        else:
            instruction = line.split(" ")[2].split("=")
            fold.append((instruction[0], int(instruction[1])))
    file.close()

def visualise_paper(x, y, points):
    paper = [["."]*(x+1) for _ in range(y+1)]
    for point in points:
        paper[point[1]][point[0]] = "#"
    for p in paper:
        line_to_print = ""
        for c in p:
            line_to_print += c
        print(line_to_print)
# PART ONE

last_x = max(i[0] for i in inputs)
last_y = max(i[1] for i in inputs)
axe_translator = {"x": 0, "y": 1}

fold_instruction = fold[0]
axe = fold_instruction[0]
fold_coordinate = fold_instruction[1]
if axe == "x":
    last_x = fold_coordinate
elif axe == "y":
    last_y = fold_coordinate
else:
    raise RuntimeError(f"Unknown axe : {axe}")
for point in inputs:
    if point[axe_translator[axe]] > fold_coordinate:
        distance = point[axe_translator[axe]] - fold_coordinate
        point[axe_translator[axe]] = point[axe_translator[axe]] - (2 * distance)


# To use set() we need an hashable type, list are not hashable but tuple are.
# Note we could have defined our own type of list and define a new __eq__ method
inputs = [tuple(i) for i in inputs]
inputs = set(inputs) # Removing duplicate points
res = len(inputs) # Number of visible points
print(f"Solution part one : {res}")

# PART TWO
# We set back to list the coordinate to support item assignement
inputs = [list(i) for i in inputs]
header = True
for fold_instruction in fold:
    if header:
        # We have done the first fold in part one 
        header = False
    else:
        axe = fold_instruction[0]
        fold_coordinate = fold_instruction[1]
        if axe == "x":
            last_x = fold_coordinate
        elif axe == "y":
            last_y = fold_coordinate
        else:
            raise RuntimeError(f"Unknown axe : {axe}")
        for point in inputs:
            if point[axe_translator[axe]] > fold_coordinate:
                distance = point[axe_translator[axe]] - fold_coordinate
                point[axe_translator[axe]] = point[axe_translator[axe]] - (2 * distance)

visualise_paper(last_x, last_y, inputs)

res = None
print(f"Solution part two : {res}")