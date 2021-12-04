import argparse
from termcolor import cprint # Import for a prettier print of boards to check if the win condition is good

parser = argparse.ArgumentParser(description='Advent of code solution.')
parser.add_argument('--test','-t', default=False, action='store_true', help='Run the example')
args = parser.parse_args()

class bingo_board:
    def __init__(self, board) -> None:
        if len(board) != 25:
            raise ValueError("The board must contain 25 values (5x5)")
        self.marked_index = []
        self.board = board
        self.last_update_value = None

    def update(self, value: int) -> None:
        self.last_update_value = value
        try:
            self.marked_index.append(self.board.index(value))
        except ValueError:
            pass # If ValueError the value is not in the board

    def check_win(self) -> bool:
        # line win
        for i in range(5):
            line_win = True
            for j in range(5):
                if 5*i+j not in self.marked_index:
                    line_win = False
                    break
            if line_win:
                return True
        # colone win
        for i in range(5):
            colone_win = True
            for j in range(5):
                if i+j*5 not in self.marked_index:
                    colone_win = False
                    break
            if colone_win:
                return True
        return False

    def reset(self)->None:
        self.marked_index = []
        self.last_update_value = None

    def score(self) -> int:
        score = 0
        for index, value in enumerate(self.board):
            if index not in self.marked_index:
                score+=value
        print(score)
        return score * self.last_update_value

    def __str__(self) -> str:
        for i in range(len(self.board)):
            if i in self.marked_index:
                color = "red"                                                                                                                                                                                        
            else:
                color = "white"
            if self.board[i] < 10:
                cprint("0", color, end="")
            cprint(str(self.board[i]), color, end="\n" if (i+1)%5==0 else " " )
        return ""


if args.test:
    numbers = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    boards = [
        bingo_board([22, 13, 17, 11,  0,
        8,  2, 23,  4, 24,
        21,  9, 14, 16,  7,
        6, 10,  3, 18,  5,
        1, 12, 20, 15, 19]),

        bingo_board([ 3, 15,  0,  2, 22,
        9, 18, 13, 17,  5,
        19,  8,  7, 25, 23,
        20, 11, 10, 24,  4,
        14, 21, 16, 12,  6]),

        bingo_board([14, 21, 17, 24,  4,
        10, 16, 15,  9, 19,
        18,  8, 23, 26, 20,
        22, 11, 13,  6,  5,
        2,  0, 12,  3,  7])
    ]
else:
    file = open("./input", "r")
    header = True
    numbers = []
    current_board = None
    boards = []
    for line in file:
        if header:
            numbers = [int(i) for i in line.strip("\n").split(",")]
            header = False
        else:
            line = line.strip("\n")
            if line == "":
                if current_board is not None:
                    boards.append(bingo_board(current_board))
                current_board = []
            else:
                for i in line.split(" "):
                    if i != "":
                        current_board.append(int(i))
                
                
    file.close()

# PART ONE
solution_found = False 
for draft_nb in numbers:
    for board in boards:
        board.update(draft_nb)
        if board.check_win():
            print(board)
            print(f"Solution 1 : {board.score()}")
            solution_found = True
        if solution_found:
            break
    if solution_found:
            break

for board in boards:
    board.reset()

# PART TWO

solution_found = False 
for draft_nb in numbers:
    boards_to_remove = []
    for board in boards:
        board.update(draft_nb)
        if board.check_win():
            if len(boards) == 1:
                print(f"Solution 2 : {boards[0].score()}")
                solution_found = True
            else:
                boards_to_remove.append(board)
        if solution_found:
            break
    for b in boards_to_remove:
        boards.remove(b)
    if solution_found:
            break
