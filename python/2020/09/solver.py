import argparse

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab=[35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,]
    key_size = 5
else:
    tab = []
    file = open("./input", "r")

    for line in file:
        tab.append(int(line.strip()))
    file.close()
    key_size = 25

# Part 1
for index in range(len(tab) - key_size-1):
    keys = tab[index:index+key_size]
    keys = sorted(keys)
    if len(set(keys)) != key_size:
        raise RuntimeError("Duplicate found in key !")
    i = tab[index+key_size]

    if i > keys[-1] + keys[-2]:
        print("Solution part 1 : ", i)
        break
    elif i < keys[0] + keys[1]:
        print("Solution part 1 : ", i)
        break
    else:
        bot = 0
        top = key_size - 1
        while keys[bot] + keys[top] != i:
            if keys[bot] + keys[top] > i:
                top -= 1
            else:
                bot +=1
            if bot == top:
                print("Solution part 1 : ", i)
                break

# Part 2
sum_elt = []
index = 0
min_index = 0
while sum(sum_elt) != i:
    sum_elt.append(tab[index])
    index += 1
    if sum(sum_elt) > i:
        sum_elt = [sum_elt[1]]
        min_index += 1
        index = min_index +1
print("Solution part 2 :", min(sum_elt) + max(sum_elt))
