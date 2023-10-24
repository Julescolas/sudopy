import sys

import error_handler as er
import checker as ch
import transformer as op


def create_list_tuple(board: list[list[int]]) -> list[(int, int, list[int])]:
    list_tuple = []
    for i in range(len(board)):
        for y in range(len(board[i])):
            if board[i][y] == 0:
                list_tuple.append((i, y, []))
    return list_tuple


def reset_already_placed_list(index:int, possible_place:list[(int, int, list[int])]):
    for i in range(index, len(possible_place)):
        possible_place[i][2].clear()
    return possible_place


def get_value_to_place(line_col: list[int], line_tab: list[int], line: list[int], already_tried: list[int]) -> (int, bool):
    value_to_place = 1
    while (not ch.can_i_put_the_number(value_to_place, line_col)
           or not ch.can_i_put_the_number(value_to_place, line_tab)
           or not ch.can_i_put_the_number(value_to_place, line)
           or not ch.can_i_put_the_number(value_to_place, already_tried)):
        value_to_place += 1
        if value_to_place > 9:
            return 0, False
    return value_to_place, True


def backtracking(board: list[list[int]], possible_place: list[(int, int, list[int])]) -> list[list[int]]:
    index = 0
    while (not ch.is_board_finish(board)):
        line_col = op.transform_col_lign(board, possible_place[index][1])
        line_tab = op.transform_square_lign(board, possible_place[index][0], possible_place[index][1])
        value, is_legal = get_value_to_place(line_col, line_tab, board[possible_place[index][0]],
                                             possible_place[index][2])
        if not is_legal:
            if index != 0:
                possible_place = reset_already_placed_list(index, possible_place)
                index -= 1
            possible_place[index][2].append(board[possible_place[index][0]][possible_place[index][1]])
            board[possible_place[index][0]][possible_place[index][1]] = 0
            continue
        else:
            board[possible_place[index][0]][possible_place[index][1]] = value
            index += 1
    return board


def stochastic(board: list[list[int]], possible_place: list[(int, int, list[int])]) -> list[list[int]]:
    return board


def sudopy(board: list[list[int]], possible_place: list[(int, int, list[int])], algoType) -> list[list[int]]:
    if algoType == 1:
        return backtracking(board, possible_place)
    if algoType == 2:
        return stochastic(board, possible_place)



try:
    start_board = er.error_handling()
    possible_place = create_list_tuple(start_board)
    final_board = sudopy(start_board, possible_place, int(sys.argv[2]))
    for lign in final_board:
        print(lign)
except Exception as e:
    print(f"Error in the except: {e}")
    exit(84)

