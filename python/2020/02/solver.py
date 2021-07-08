# FILE READING
file = open("./input", "r")
nb_correct_pwd = 0
max = 0
min = 0
letter = ""
tab = []
for line in file:
    rule, pwd = line.split(":")
    min_max, letter = rule.split(" ")
    min, max = min_max.split("-")
    tab.append((min, max, letter, pwd))        
file.close()

# PART ONE
for value in tab:
    min, max, letter, pwd = value
    count = 0
    for l in pwd:
        if l == letter:
            count += 1
    if int(min) <= count <= int(max):
        nb_correct_pwd += 1
print("Nombre de mot de passe non corrompu :", nb_correct_pwd)

# PART TWO
nb_correct_pwd = 0

for value in tab:
    min, max, letter, pwd = value
    max=int(max)
    min=int(min)
    if not ((pwd[min] == letter and pwd[max] == letter) or (pwd[min] != letter and pwd[max] != letter)):
        nb_correct_pwd += 1
print("Nombre de mot de passe non corrompu :", nb_correct_pwd)
