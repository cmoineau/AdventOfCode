tab = []
file = open("./input", "r")
for line in file:
    tab.append(line.strip())
file.close()

# PART ONE
lane_size = len(tab[0])


def tree_hit(r, d):
    cpt = 0
    i = 0
    j = 0
    for j in range(0, len(tab), d):
        if tab[j][i%lane_size] == '#':
            cpt += 1
        i += r
    return cpt

print(tree_hit(3, 1))

# PART TWO


print(tree_hit(1, 1) * tree_hit(3, 1) * tree_hit(5, 1) * tree_hit(7, 1) * tree_hit(1, 2))
