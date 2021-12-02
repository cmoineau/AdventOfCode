import argparse
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
else:
    tab = []
    file = open("./input", "r")
    for line in file:
        tab.append(int(line.strip("\n")))
    file.close()

# PART ONE

counter = 0
j = None
for i in tab:
    if j is not None and i > j:
        counter += 1
    j = i
    
print(f"Part ONE : {counter}") 

# PART TWO

counter = 0
j = None
for i in range(0, len(tab)-3):
    a = tab[i]
    b = tab[i+3]
    if b > a:
        counter += 1
print(f"Part TWO : {counter}") 