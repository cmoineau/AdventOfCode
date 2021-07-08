tab = []
file = open("./input", "r")
for line in file:
    tab.append(line.strip())
file.close()

#PART ONE
dico = {"byr" : False, "iyr" : False, "eyr" : False, "hgt" : False, "hcl" : False, "ecl" : False, "pid" : False, "cid" : False}

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

cpt = 0
for line in tab:
    if line == "":
        valid = True
        for key, present in dico.items():
            if key != "cid":
                valid = valid & present
        if valid:
            cpt += 1
        dico = {"byr" : False, "iyr" : False, "eyr" : False, "hgt" : False, "hcl" : False, "ecl" : False, "pid" : False, "cid" : False}
    else:
        key_values = line.split(' ')
        for key_value in key_values:
            k, value = key_value.split(':')
            dico[k] = True
print("First part answer : ", cpt)
#PART TWO

number = ["0","1","2","3","4","5","6","7","8","9"]
letter = ["a","b","c","d","e","f"]
eycol =  ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
cpt = 0
dico = {"byr" : False, "iyr" : False, "eyr" : False, "hgt" : False, "hcl" : False, "ecl" : False, "pid" : False, "cid" : False}

for line in tab:
    if line == "":
        valid = True
        for key, present in dico.items():
            if key != "cid":
                valid = valid & present
        if valid:
            cpt += 1
        dico = {"byr" : False, "iyr" : False, "eyr" : False, "hgt" : False, "hcl" : False, "ecl" : False, "pid" : False, "cid" : False}
    else:
        key_values = line.split(' ')
        for key_value in key_values:
            k, v = key_value.split(':')
            if k == "byr" and 1920 <= int(v) <= 2002:
                dico[k] = True
            if k == "iyr" and 2010 <= int(v) <= 2020:
                dico[k] = True
            if k == "eyr" and 2020 <= int(v )<= 2030:
                dico[k] = True
            if k == "hgt":
                num = v[:len(v)-2]
                s = v[-2:]
                if s == "cm" and 150<=int(num)<=193:
                    dico[k] = True
                elif s == "in" and 59<=int(num)<=76:
                    dico[k] = True

            if k == "hcl":
                if v[0] == "#" and len(v[1:]) == 6 and (sum([(i in number or i in letter) for i in v[1:]]) == 6):
                    dico[k] = True
                        
            if k == "ecl" and v in eycol:
                dico[k] = True
                
            if k =="pid":
                if len(v) == 9 and sum([i in number for i in v]) == 9:
                    dico[k] = True
print("Second part answer", cpt)
