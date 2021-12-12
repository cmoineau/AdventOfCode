import argparse
from math import floor, ceil
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')

args = parser.parse_args()


if args.test:
    tab = [
        ["be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb", "fdgacbe cefdb cefbgd gcbe"],
        ["edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec", "fcgedb cgb dgebacf gc"],
        ["fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef", "cg cg fdcagb cbg"],
        ["fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega", "efabcd cedba gadfec cb"],
        ["aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga", "gecf egdcabf bgf bfgea"],
        ["fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf", "gebdcfa ecba ca fadegcb"],
        ["dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf", "cefg dcbef fcge gbcadfe"],
        ["bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd", "ed bcgafe cdgba cbgef"],
        ["egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg", "gbdfcae bgc cg cgb"],
        ["gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc", "fgae cfgab fg bagce"]
    ]

else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab.append(line.strip("\n").split("|"))             
    file.close()

nb_easy_digits = 0
for signal_digit in tab: 
    signals, digits = signal_digit
    for digit in digits.split(" "):
        if len(digit) == 2: # 1 digit
            nb_easy_digits += 1
        elif len(digit) == 4: # 4 digit
            nb_easy_digits += 1
        elif len(digit) == 3: # 7 digit
            nb_easy_digits += 1
        elif len(digit) == 7: # 8 digit
            nb_easy_digits += 1

print("Solution part one :", nb_easy_digits)

tab_test = [
        ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab", "cdfeb fcadb cdfeb cdbaf"],]

def reorder_signal(signal):
    return sorted(signal)

def solver(signals, digits):
    mapping = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8: "abcdefg", 9:""}
    for signal in sorted(signals.split(" "), key=len): # We sort by len to get 1, 7, 4 first this would help us decypher the other digits
        signal = sorted(signal)
        if len(signal) == 2: # 1 digit
            mapping[1] = signal
        elif len(signal) == 4: # 4 digit
            mapping[4] = signal
        elif len(signal) == 3: # 7 digit
            mapping[7] = signal
        elif len(signal) == 7: # 8 digit
            mapping[8] = signal
        elif len(signal) == 5: # 2, 3 or 5 digit
            is_three = True
            for letter in mapping[1]:  # Three is the only 6 segments to contain the segments of 1
                if letter not in signal:
                    is_three = False
            if is_three:
                mapping[3] = signal
            else:
                is_five_condition = 0 # If the value of this variable is 3 we have a 5 else a 2
                for letter in mapping[4]:
                    if letter in signal:
                        is_five_condition += 1
                if is_five_condition == 3:
                    mapping[5] = signal
                else:
                    mapping[2] = signal
        elif len(signal) == 6: # 0, 6 or 9 digit
            is_six = False
            for letter in mapping[1]: # 6 is the only 6 segments to not contains the segments of 1
                if letter not in signal:
                    is_six = True
            if is_six:
                mapping[6] = signal
            else:
                is_nine = True # 9 contains the segments of 5 and 0 doesn't and we decyphered 5 first because we sorted by len !
                for letter in mapping[5]:
                    if letter not in signal:
                        is_nine = False
                if is_nine:
                    mapping[9] = signal
                else:
                    mapping[0] = signal

    value = ""
    for digit in digits.split(' '):
        digit = sorted(digit)
        for k, v in mapping.items():
            if v == digit:
                value += str(k)
    return int(value)

solution = 0
for signal_digit in tab:
    signals, digits = signal_digit
    solution += solver(signals, digits)

print(f"Solution part TWO : {solution}")