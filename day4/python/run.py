with open("input.txt") as f:
    lines = f.read().splitlines()

all_numbers = [int(num) for num in lines[0].split(",")]

boards = []
for i in range(2, len(lines), 6):
    board = [[int(num) for num in line.split()] for line in lines[i : i + 5]]
    boards.append(board)


def is_complete(board, numbers):
    def all_played(*line):
        return all((num in numbers) for num in line)

    if (
        # check all rows
        all_played(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4])
        or all_played(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4])
        or all_played(board[2][0], board[2][1], board[2][2], board[2][3], board[2][4])
        or all_played(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4])
        or all_played(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4])
        # check all columns
        or all_played(board[0][0], board[1][0], board[2][0], board[3][0], board[4][0])
        or all_played(board[0][1], board[1][1], board[2][1], board[3][1], board[4][1])
        or all_played(board[0][2], board[1][2], board[2][2], board[3][2], board[4][2])
        or all_played(board[0][3], board[1][3], board[2][3], board[3][3], board[4][3])
        or all_played(board[0][4], board[1][4], board[2][4], board[3][4], board[4][4])
    ):
        return True

    return False


def unplayed_numbers(board, numbers):
    unplayed_numbers = []
    for line in board:
        for num in line:
            if not num in numbers:
                unplayed_numbers.append(num)
    return unplayed_numbers


def winning_board(boards, all_numbers):
    numbers = {
        all_numbers[0],
        all_numbers[1],
        all_numbers[2],
        all_numbers[3],
    }

    winning_board = None
    while not winning_board:
        numbers.add(all_numbers[len(numbers)])
        for board in boards:
            if is_complete(board, numbers):
                winning_board = board
                break
    return board, numbers


def last_played_number(numbers, all_numbers):
    return all_numbers[len(numbers) - 1]


def score(board, numbers, all_numbers):
    sum_of_unplayed = sum(unplayed_numbers(board, numbers))
    last_played = last_played_number(numbers, all_numbers)

    return sum_of_unplayed * last_played


winning_board, winning_numbers = winning_board(boards, all_numbers)
print(f"q1: score - {score(winning_board, winning_numbers, all_numbers)}")


def losing_board(boards, all_numbers):
    numbers = {
        all_numbers[0],
        all_numbers[1],
        all_numbers[2],
        all_numbers[3],
    }

    left_prev = boards
    while True:
        numbers.add(all_numbers[len(numbers)])
        left = [b for b in boards if not is_complete(b, numbers)]

        if len(left) == 0 and len(left_prev) == 1:
            losing_board = left_prev[0]
            break

        left_prev = left
    return losing_board, numbers

loser, losing_numbers = losing_board(boards, all_numbers)
print(f"q2: score - {score(loser, losing_numbers, all_numbers)}")
