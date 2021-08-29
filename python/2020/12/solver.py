import argparse
from math import cos, sin, radians

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

if args.test:
    tab=[
        ("F", 10),
        ("N",3),
        ("F", 7),
        ("R", 90),
        ("F", 11),
    ]
else:
    tab = []
    file = open("./input", "r")
    tab=[(line[0], int(line[1:].strip("\n"))) for line in file]
    file.close()

# Part 1

angle_converter = {
    0  : "E",
    90 : "S",
    180: "W",
    270: "N"
}

def part1(tab):
    x = 0
    y = 0
    current_angle = 0
    for instruction in tab:
        action, value= instruction
        if action == "F":
            action = angle_converter[current_angle]

        if action == "N":
            x += value
        elif action == "S":
            x -= value
        elif action == "E":
            y += value
        elif action == "W":
            y -= value
        elif action == "L":
            current_angle = (current_angle - value)%360
            if current_angle < 0:
                current_angle += 360
        elif action == "R":
            current_angle = (current_angle + value)%360
        else:
            raise RuntimeError("action not recognized " + action)
    return x, y

x, y = part1(tab)
print("Solution part 1", abs(x) + abs(y))

# Part 2 

def part2(tab):
    x = 0; y = 0; wp_x = 1; wp_y = 10
    for instruction in tab:
        action, value = instruction
        if action == "F":
            x += wp_x * value
            y += wp_y * value
        elif action == "N":
            wp_x += value
        elif action == "S":
            wp_x -= value
        elif action == "E":
            wp_y += value
        elif action == "W":
            wp_y -= value
        elif action == "L":
            value = radians(value)
            tmp = wp_x
            wp_x = wp_x * cos(-value) - wp_y * sin(-value)
            wp_y = tmp * sin(-value) + wp_y * cos(-value)
        elif action == "R":
            value = radians(value)
            tmp = wp_x
            wp_x = wp_x * cos(value) - wp_y * sin(value)
            wp_y = tmp * sin(value) + wp_y * cos(value)
        else:
            raise RuntimeError("action not recognized " + action)
    return x, y

x, y = part2(tab)
print("Solution part 2", int(abs(x) + abs(y)))