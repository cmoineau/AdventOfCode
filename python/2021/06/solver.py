import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()


if args.test:
    tab = [3,4,3,1,2]

else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab += [int(i) for i in line.strip("\n").split(",")]               
    file.close()

# PART ONE

dico = {} # Key : counter before giving brith | Value : number of fish
for i in range(9):
    dico[i] = 0

for i in tab:
    dico[i] += 1

for i in range(256): # Simulating the 80 days
    # print(f"Day #{i} : number of fish :{sum(dico.values())}")
    number_new_fish = dico[0] 
    for j in range(1, 9):
        dico[j-1]=dico[j]
    dico[8] = number_new_fish
    dico[6] += number_new_fish
    if i == 79:
        print(f"Solution  part one : {sum(dico.values())}")

print(f"Solution  part two : {sum(dico.values())}")
