tab = []
file = open("./input", "r")

for line in file:
    tab.append(int(line.strip()))
file.close()



# PART 1
preamble = tab[:25]
preamble.sort()
datas = tab[25:]

def recombulator(number, tab=preamble):
    min = 0
    max = len(tab) -1
    while tab[min] + tab[max] != number and min != max:
        if tab[min] + tab[max] < number:
            min += 1
        else:
            max -= 1
    if tab[min] + tab[max] != number:
        return False
    else:
        return True

maximum = preamble[-1] + preamble[-2]
minimum = preamble[0] + preamble[1]


for data in datas:
    if (not minimum<data<maximum):
        print('0Answer :', data)
        break
    if recombulator(data):
        print('1Answer :', data)
        break
        
    
