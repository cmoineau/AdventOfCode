import argparse
from copy import deepcopy
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    timestamp = 939
    bus_id = ["7","13","x","x","59","x","31","19"]
else:
    tab = []
    file = open("./input", "r")

    for line in file:
        tab.append(line.strip("\n"))
    timestamp = int(tab[0])
    bus_id = tab[1].split(',')
    file.close()

# Part 1
min_id = None
min_wait = None
for id in bus_id:
    if id!="x":
        id = int(id)
        wait = id - (timestamp%id)
        if min_wait is None or min_wait > wait:
            min_wait = wait
            min_id = id

print(f'Solution part 1 : {min_id * min_wait}')

# Part 2

bus_offset = [(i, int(j)) for i, j in enumerate(bus_id) if j != "x"]

new_timestamp = 0
product = 1

for offset, bus_id in bus_offset:
    flag = True # Emulating a do-while loop
    while flag or ((new_timestamp+offset) % bus_id) != 0:
        new_timestamp += product
        flag = False
    product *= bus_id

print(f'Solution part 2 : {new_timestamp}')
