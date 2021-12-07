import argparse
from math import floor, ceil
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()


if args.test:
    tab = [16,1,2,0,4,2,7,1,2,14]

else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab += [int(i) for i in line.strip("\n").split(",")]               
    file.close()

# PART ONE
tab.sort()
median = tab[int(len(tab)/2)]
result = sum([abs(i-median) for i in tab])
print("Solution part one : ", result)

from statistics import mean 
# PART TWO
tab.sort()
avg = sum(tab)/float(len(tab))

avg1 = ceil(avg)
avg2 = floor(avg)

result1 = sum([(abs(avg1-i)*(abs(avg1-i)+1)/2) for i in tab])
result2 = sum([(abs(avg2-i)*(abs(avg2-i)+1)/2) for i in tab])

print("Solution part two : ", min(result1, result2))