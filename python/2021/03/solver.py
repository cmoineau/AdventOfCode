import argparse
from math import floor, ceil
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab = [ 
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"]
else:
    tab = []
    file = open("./input", "r")
    for line in file:
        tab.append(line.strip("\n"))
    file.close()

# PART ONE
number_of_data = len(tab)
bits_sum = [0] * len(tab[0])
for bin in tab:
    for bit_idx in range(len(bin)):
        bits_sum[bit_idx] += int(bin[bit_idx])

e_rate = ''
g_rate = ''

for sum in bits_sum:
    if sum < int(number_of_data/2): # 0 is more common at this index
        e_rate += "1"
        g_rate += "0"
    else: # 1 more common at this index
        e_rate += "0"
        g_rate += "1"
print(f"gamma : {g_rate}; epsilon : {e_rate}")
gamma = int(g_rate, 2)
epsilon = int(e_rate, 2)
print(f"gamma : {int(g_rate, 2)}; epsilon : {int(e_rate, 2)}")
print(f"Solution part ONE : ", gamma*epsilon)

def sum_index(list_input, idx):
    sum = 0
    for i in list_input:
        sum += int(i[idx])
    return sum

# PART TWO
O_candidate = [i for i in tab]
CO2_candidate = [i for i in tab] 

for bit_index in range(len(tab[0])):
    if len(O_candidate) != 1:
        O_survivor = []
        O_criteria = "0" if sum_index(O_candidate, bit_index) < ceil(len(O_candidate)/2) else "1"
        for o in O_candidate:
            if o[bit_index] == O_criteria:
                O_survivor.append(o)
        O_candidate = O_survivor
    if len(CO2_candidate) != 1:
        CO2_survivor = []
        CO2_criteria = "0" if sum_index(CO2_candidate, bit_index) >= ceil(len(CO2_candidate)/2) else "1" 
        for co2 in CO2_candidate:
            if co2[bit_index] == CO2_criteria:
                CO2_survivor.append(co2)
        CO2_candidate = CO2_survivor

if len(O_candidate) != len(CO2_candidate) != 1:
    raise ValueError("Len should be 1")
o_value = int(O_candidate[0], 2)
co2_value = int(CO2_candidate[0], 2)
print(f"O {O_candidate[0]}, CO2 {CO2_candidate[0]}")
print(f"O {o_value}, CO2 {co2_value}")
print(f"Part 2 solution : {o_value * co2_value}")