import checker as ch
import random
def get_random_value(list: list[int]):
    random.shuffle(list)
    if len(list) == 0:
        t = 2
    value = list.pop()
    return value, list

def find_possible_number_by_line(board: list[list[int]]) -> list[list[int]]:
    possible_numbers = []
    for lign in board:
        possible_numbers_line = []
        for i in range(1,10):
            if ch.can_i_put_the_number(i, lign):
                possible_numbers_line.append(i)
        possible_numbers.append(possible_numbers_line)
    return possible_numbers


def clear_values(board:list[list[int]], possible_place:list[(int,int,list[int])]) -> list[list[int]]:
    for place in possible_place:
        board[place[0]][place[1]] = 0
    return board


def stochastic(board: list[list[int]], possible_place: list[(int, int, list[int])]) -> list[list[int]]:
    while ch.find_all_error(board) != 0:
        print(ch.find_all_error(board))
        board = clear_values(board, possible_place)
        possible_numbers = find_possible_number_by_line(board)
        for place in possible_place:
            board[place[0]][place[1]], possible_numbers[place[0]] = get_random_value(possible_numbers[place[0]])

    return board
