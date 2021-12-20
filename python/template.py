import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()
if args.test:
    # TEST INPUT
    input = []
else:
    # PARSING INPUT FILE
    file = open("./input", "r")
    input = []
    for line in file:
        input.append(line.strip("\n"))             
    file.close()

# PART ONE

res = None
print(f"Solution part one : {res}")

# PART TWO

res = None
print(f"Solution part two : {res}")