tab = []
file = open("./input", "r")
for line in file:
    tab.append(int(line.strip()))
file.close()

tab.sort()
print(tab)

# PART ONE
min = 0
max = len(tab) -1
while tab[min] + tab[max] != 2020 and min != max:
    if tab[min] + tab[max] < 2020:
        min += 1
    else:
        max -= 1
if tab[min] + tab[max] != 2020:
    print("Pas de solution.")
else:
    print("Solution :", tab[min] * tab[max])
    
# PART TWO
# Brute force ...
for i in range(len(tab)-2):
    for j in range(1,len(tab)-1):
        for k in range(2,len(tab)):
            if tab[i] + tab[j] + tab[k] == 2020:
                print("Solution :", tab[i] * tab[j] * tab[k])
