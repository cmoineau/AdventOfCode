import argparse
parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
parser.add_argument('-v', default=False, action='store_true', help='Visualise diagram')
args = parser.parse_args()
if args.test:
    tab = [ "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]"]
else:
    file = open("./input", "r")
    tab = []
    for line in file:
        tab.append(line.strip("\n"))             
    file.close()
opening_char = ["[", "(", "{", "<"]
closing_char = ["]", ")", "}", ">"]

open_close_map = {"[": "]", "(":")", "{": "}", "<": ">"}
part_one_values = {"]":57, ")":3, "}":1197, ">":25137}
part_two_values = {"]":2, ")":1, "}":3, ">":4}
res_part_one = 0
part_two_scores = []
for char in tab:
    to_close = []
    wrong_char = None
    for c in char:
        if c in opening_char:
            to_close.append(open_close_map[c])
        elif c in closing_char:
            close_c = to_close.pop()
            if c != close_c:
                # print(f"{char} - Expected '{close_c}' got '{c}' instead")
                wrong_char = c
                break
        else:
            RuntimeError(f"Unrecognized char : {c}")
    if wrong_char is not None:
        # Corrupted line
        res_part_one += part_one_values[wrong_char]
    else:
        # print(f"{char} - Comple by adding {to_close}")
        score = 0
        for c in reversed(to_close): # Reversed because we acces this list with pop
            score = score * 5 + part_two_values[c]
        part_two_scores.append(score)
print(f"SOLUTION PART ONE : {res_part_one}")
print(f"SOLUTION PART TWO : {sorted(part_two_scores)[int(len(part_two_scores)/2)]}")