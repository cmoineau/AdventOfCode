from copy import deepcopy
heap = []
file = open("./input", "r")

for line in file:
    heap.append(line.strip().split(' '))
file.close()

# TEST
# heap = [
# ["nop", "+0"],
# ["acc", "+1"],
# ["jmp", "+4"],
# ["acc", "+3"],
# ["jmp", "-3"],
# ["acc", "-99"],
# ["acc", "+1"],
# ["jmp", "-4"],
# ['acc', '+6']]


# PART 1

def run_heap(heap):
    acc = 0
    i = 0
    index_historic = []
    while i < len(heap):
        if i in index_historic:
            return None
        index_historic.append(i)
        instruction = heap[i]
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            i += 1
        elif instruction[0] == 'jmp':
            i += int(instruction[1])
        elif instruction[0] == 'nop':
            i+=1
    return acc
print("Accumulator : ", run_heap(heap))

# PART 2

for index in range(len(heap)):
    if heap[index][0] == "nop":
        testing_heap = deepcopy(heap)
        testing_heap[index][0] = "jmp"
    elif heap[index][0] == "jmp":
        testing_heap = deepcopy(heap)
        testing_heap[index][0] = "nop"
    else:
        continue

    result = run_heap(testing_heap)
    if result:
        print("Result : ", result)

