import argparse
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab = [ ("forward", 5),
            ("down", 5),
            ("forward", 8),
            ("up", 3),
            ("down", 8),
            ("forward", 2)]
else:
    tab = []
    file = open("./input", "r")
    for line in file:
        command, value = line.strip("\n").split(" ")
        tab.append((command, int(value)))
    file.close()

# PART ONE

x = 0 # position
y = 0 # depth

for i in tab:
    command, value = i
    # control_panel[command](value)
    if command == "up":
        y-=value
    elif command == "down":
        y+=value
    elif command == "forward":
        x+=value

print(f"PART ONE : {x*y}")

# PART TWO

x = 0 # position
y = 0 # depth
aim = 0

for i in tab:
    command, value = i
    if command == "up":
        aim-=value
    elif command == "down":
        aim+=value
    elif command == "forward":
        x+=value
        y+=(aim*value)

print(f"PART TWO : {x*y}")