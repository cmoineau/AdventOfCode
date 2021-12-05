import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()


if args.test:
    lines = [
    ((0, 9), (5, 9)),
    ((8, 0), (0, 8)),
    ((9, 4), (3, 4)),
    ((2, 2), (2, 1)),
    ((7, 0), (7, 4)),
    ((6, 4), (2, 0)),
    ((0, 9), (2, 9)),
    ((3, 4), (1, 4)),
    ((0, 0), (8, 8)),
    ((5, 5), (8, 2))]

else:
    file = open("./input", "r")
    lines = []
    for line in file:
        split = line.split(" -> ")
        xy1= [int(i) for i in split[0].split(',')]
        xy2= [int(i) for i in split[1].split(',')]
        lines.append((xy1, xy2))
                
    file.close()

# PART ONE
max_x, max_y = 0, 0
covered_coordinates = {} # Dictionnaries with coordinates as key and a counter of appearance as value
for line in lines:
    xy1, xy2 = line
    x1, y1 = xy1
    x2, y2 = xy2
    max_x = max(max_x, x1)
    max_x = max(max_x, x2)
    max_y = max(max_y, y1)
    max_y = max(max_y, y2)
    if x1 == x2: # Horizontal 
        for tmp_y in range(min(y1,y2), max(y1,y2)+1):
            if (x1, tmp_y) in covered_coordinates:
                covered_coordinates[(x1, tmp_y)] += 1
            else:
                covered_coordinates[(x1, tmp_y)] = 1
    if y1 == y2: # Vertical
        for tmp_x in range(min(x1,x2), max(x1,x2)+1):
            if (tmp_x, y1) in covered_coordinates:
                covered_coordinates[(tmp_x, y1)] += 1
            else:
                covered_coordinates[(tmp_x, y1)] = 1

cpt = 0

for key, value in covered_coordinates.items():
    if value > 1:
        cpt += 1
print(f"Solution 1 : {cpt}")

if args.v:
    for j in range(max_x+1):
        current_line = ""
        for i in range(max_y+1):
            if (i, j) in covered_coordinates:
                current_line += str(covered_coordinates[(i,j)])
            else:
                current_line += "."
        print(current_line)

# Part TWO 

for line in lines:
    xy1, xy2 = line
    x1, y1 = xy1
    x2, y2 = xy2
    if x1 != x2 and y1 != y2: # Diagonal 
        x_sign = 1 if x1 < x2 else -1
        y_sign = 1 if y1 < y2 else -1
        for tmp_y, tmp_x in zip(range(y1, y2+y_sign, y_sign), range(x1, x2+x_sign, x_sign)):
            if (tmp_x, tmp_y) in covered_coordinates:
                if tmp_x == 5 and tmp_y == 4:
                    print(xy1, xy2)
                covered_coordinates[(tmp_x, tmp_y)] += 1
            else:
                if tmp_x == 5 and tmp_y == 4:
                    print(xy1, xy2)
                covered_coordinates[(tmp_x, tmp_y)] = 1
        
cpt = 0

for key, value in covered_coordinates.items():
    if value > 1:
        cpt += 1

# Diagram visualisation
if args.v:
    for j in range(max_x+1):
        current_line = ""
        for i in range(max_y+1):
            if (i, j) in covered_coordinates:
                current_line += str(covered_coordinates[(i,j)])
            else:
                current_line += "."
        print(current_line)
cpt = 0
for key, value in covered_coordinates.items():
    if value > 1:
        cpt += 1
print(f"Solution 2 : {cpt}")
