import argparse
from functools import reduce, cache
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Enable verbose')

args = parser.parse_args()
if args.test:
    # TEST INPUT
    parsed_input = [[3, 4, 2, 1, 3, 3,], [4, 3, 5, 3, 9, 3]]

else:
    # PARSING INPUT FILE
    file = open("./input", "r")
    parsed_input = [[], []]
    for line in file:
        l1, l2 = line.strip("\n").split("   ")
        parsed_input[0].append(int(l1))
        parsed_input[1].append(int(l2))    
    file.close()
# PART ONE

ordered_inputs = []
if args.v: print(f"Sorting 1st list ...")
ordered_inputs.append(sorted(parsed_input[0]))
if args.v: print(f"Sorting 2nd list ...")
ordered_inputs.append(sorted(parsed_input[1]))
if args.v: print(f"Computing distance ...")

dist_input = [abs(i-j) for i,j in zip(ordered_inputs[0], ordered_inputs[1])]

res = reduce(lambda x,y: x+y, dist_input)
print(f"Solution part one : {res}")

# PART TWO
res = 0

@cache
def nb_appearance(value):
    nb_app = 0
    for i in parsed_input[1]:
        nb_app += (i == value)
    return nb_app

for j in parsed_input[0]:
    res += j * nb_appearance(j)

print(f"Solution part two : {res}")