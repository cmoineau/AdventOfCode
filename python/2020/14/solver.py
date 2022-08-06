import argparse
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]
else:
    tab = []
    file = open("./input", "r")
    for line in file:
        tab.append(line.strip("\n"))
    file.close()



# Part 1
def apply_mask(value, mask):
    masked_value = ""
    for v, m in zip(value, mask):
        if m == "X":
            masked_value += v
        else:
            masked_value += m
    return masked_value

def read_memory(string):
    result = 0
    for index in reversed(range(len(enumerate(string)))):
        if string[index] == '1':
            result += 2**index
    return result

memory = [0 for _ in range(36)]
new_mask = None
for instruction in tab:
    if instruction[:3] == "mas":
        new_mask = instruction.split("=")[-1].strip(" ")
    elif instruction[:3] == "mem":
        if new_mask is None:
            raise RuntimeError("We missed the mask !")
        value =  str(bin(int(instruction.split("=")[-1].strip(" "))))
        value =  value.replace("0b", "")
        value = ("0"*(32-len(value))) + value
        addr = int(instruction.split("[")[1].split("]")[0])
        print(value)
        masked_value = apply_mask(value, new_mask)
        print(masked_value)
        memory[addr] = masked_value
    else:
        raise ValueError("Instruction not recognized !")

print(read_memory("00000000000000000000000000001011"))
