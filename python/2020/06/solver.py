from collections import Counter
tab = []
file = open("./input", "r")
res = 0
groupe = []
for line in file:
    line = line.strip()
    if line != "":
        for e in line:
            groupe.append(e)
    else:
        res += len(set(groupe))
        groupe = []
file.close()
print('1 :', res)

tab = []
file = open("./input", "r")
res = 0
cpt = 0
groupe = []
for line in file:
    line = line.strip()
    if line != "":
        for e in line:
            groupe.append(e)
        cpt += 1
    else:
        counted  = Counter(groupe)
        for c in counted:
            if counted[c] == cpt:
                res += 1
        groupe = []
        cpt = 0
file.close()
print('2': res)
