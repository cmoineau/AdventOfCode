tab = []
file = open("./input", "r")

for line in file:
    id, rules = line.strip().split(" contain")
    tab.append([id.split(" bag")[0], rules])
file.close()


can_contain = ["shiny gold"]
updated = True

while updated:
    updated = False
    for rules in tab:
        if rules[0] not in can_contain:
            if sum([t in rules[1] for t in can_contain]) > 0:
                can_contain.append(rules[0].split(" bag")[0])
                updated = True
print("part 1 : ", len(can_contain)-1)

# PART TWO


dico_color = {}

for t in tab:
    dico_color[t[0]] = []
    colors_nb = t[1].split(',')
    for i in colors_nb:
        if "no other" in i:
            nb = 0
            color = "no other"
        else:
            nb = int(i.split(' ')[1])
            color = i.split(' ')[2] + ' ' +i.split(' ')[3]
            
        dico_color[t[0]].append([nb, color])

def rec(color):
    res = 0
    if color != "no other":
        for c in dico_color[color]:
            res += c[0] + (c[0] * rec(c[1]))
            if color =="shiny gold":
    else:
        res = 1
    return res 

print("part2", rec("shiny gold"))
