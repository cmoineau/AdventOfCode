import argparse
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    # tab=[16,
    #     10,
    #     15,
    #     5,
    #     1,
    #     11,
    #     7,
    #     19,
    #     6,
    #     12,
    #     4 ,]
    tab=[28,
        33,
        18,
        42,
        31,
        14,
        46,
        20,
        48,
        47,
        24,
        23,
        49,
        45,
        19,
        38,
        39,
        11,
        1,
        32,
        25,
        35,
        8,
        17,
        7,
        9,
        4,
        2,
        34,
        10,
        3,]
else:
    tab = []
    file = open("./input", "r")

    for line in file:
        tab.append(int(line.strip()))
    file.close()

built_in_volt = max(tab) + 3

print(f"built_in_volt : {built_in_volt:d}")

print("Sorting the adaptaters ...")
tab.sort()


onev_skip = 0
twov_skip = 0
threev_skip = 0

current_v = 0 

# PART 1
for i in tab:
    if i > current_v + 3:
        raise RuntimeError("Can't connect all adaptaters !")
    else:
        if i - current_v == 1:
            onev_skip +=1 
        elif i - current_v == 2:
            twov_skip += 1
        else:
            threev_skip += 1
        current_v = i

if onev_skip + twov_skip + threev_skip != len(tab):
    raise RuntimeError(f"The total number of skip doesn't correspond with the number of adapataters : {(onev_skip + twov_skip + threev_skip):d} != {len(tab):d}")

# Connecting our monitor :
threev_skip += 1

print(f"Solution part 1 : {onev_skip*threev_skip:d}")

# PART 2

# Because we risk to compute the number of possibilities for the same voltage we want to store the results. 
cache = {}

def recursive(adaptater_list, current_v):
    if current_v in cache:
        return cache[current_v]
    if current_v + 3 == built_in_volt:
        return 1
    nb_sol = 0
    # Adaptaters voltage is unique thus by sorting we ensure that at best we can connect to the 3 nexts adaptaters
    # Tests are imbricates becuase if one fail the other will
    if len(adaptater_list) >= 1 and adaptater_list[0] - current_v <= 3:
        nb_sol += recursive(adaptater_list[1:], adaptater_list[0])
        if len(adaptater_list) >= 2 and adaptater_list[1] - current_v <= 3 :
            nb_sol += recursive(adaptater_list[2:], adaptater_list[1])
            if len(adaptater_list) >= 3 and adaptater_list[2] - current_v <= 3:
                nb_sol += recursive(adaptater_list[3:], adaptater_list[2])
    else:
        return 0
    cache[current_v] = nb_sol
    return nb_sol
print(f"Solution part 2 : {recursive(tab, 0):d}")
