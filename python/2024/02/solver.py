import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Enable verbose mode?')

args = parser.parse_args()
if args.test:
    # TEST INPUT
    parsed_input = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]]

else:
    # PARSING INPUT FILE
    file = open("./input", "r")
    parsed_input = []
    for line in file:
        parsed_input.append([int(i) for i in line.strip("\n").split(" ")])             
    file.close()
print(parsed_input)
# PART ONE

def level_reader(level):
    flag_increase = level[0] - level[1] > 0
    for i in range(1, len(level)):
        if flag_increase != (level[i-1] - level[i] > 0):
            return False
        if not (0 < abs(level[i-1] - level[i]) <= 3):
            return False
    return True
res = 0

for level in parsed_input:
    res += level_reader(level)
    if args.v: print(f"{level}: {level_reader(level)}")

print(f"Solution part one : {res}")

# PART TWO
def level_reader_v2(a):
    ok = level_reader(a)
    if not ok:
        for i in range(len(a)):
            b = []
            for j in range(len(a)):
                if i!=j: b.append(a[j])
            ok = level_reader(b)
            if ok: break
    return ok
res = 0
for level in parsed_input:
    res += level_reader_v2(level)
    if args.v: print(f"{level}: {level_reader_v2(level)}")

print(f"Solution part two : {res}")