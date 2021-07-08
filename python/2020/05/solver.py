tab = []
file = open("./input", "r")
for line in file:
    tab.append(line.strip())
file.close()
import math
m = 0
seats_id = []
#tab = ["FBFBBFFRLR", "BFFFBBFRRR","FFFBBBFRRR", "BBFFBBFRLL"]
#PART ONE
for r in tab:
    a = [0,127]
    for l in r[:7]:
        if l == "F":
            a[1] = math.floor((a[1] + a[0])/2)
        elif l == "B":
            a[0] = math.ceil((a[1] + a[0])/2)
        else:
            raise ValueError("ERROR: Unexpected argument :", l)
    res = 0
    if r[6] == "F":
        res = a[0]
    else:
        res = a[1]
    a = [0,7]
    for l in r[7:]:
        if l == "L":
            a[1] =  math.floor((a[1] + a[0])/2)
        elif l == "R":
            a[0] =  math.ceil((a[1] + a[0])/2)
        else:
            raise ValueError("ERROR: Unexpected argument :", l)
    
    if r[-1] == "R":
        res = res * 8 + a[1]
    else:
        res = res * 8 + a[0]
    seats_id.append([r, res])
seats_id = sorted(seats_id, key=lambda x: x[1])

print(seats_id[-1][1])
#PART TWO
previous = -1
for i in range(len(seats_id)-1) :
    if i != 0 or i != len(seats_id):
        if seats_id[i-1][1] != seats_id[i][1] - 1:
            print('m', seats_id[i][0], seats_id[i][1])
        if seats_id[i+1][1] != seats_id[i][1] + 1:
            print('p', seats_id[i][0], seats_id[i][1])
    #if previous != -1:
        #if previous_1 != -1:
            #if previous_1 != previous -1 or id[1] != previous +1:
                #print(id)
            #previous_1 = previous
            #previous = id[1]
        #else:
            #previous_1 = id[1]
    #else:
        #previous = id[1]
