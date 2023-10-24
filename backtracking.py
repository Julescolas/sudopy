import transformer as op
import checker as ch
import utils as us

def backtracking(board: list[list[int]], possible_place: list[(int, int, list[int])]) -> list[list[int]]:
    index = 0
    while (not ch.is_board_finish(board)):
        line_col = op.transform_col_lign(board, possible_place[index][1])
        line_tab = op.transform_square_lign(board, possible_place[index][0], possible_place[index][1])
        value, is_legal = us.get_value_to_place(line_col, line_tab, board[possible_place[index][0]],
                                             possible_place[index][2])
        if not is_legal:
            if index != 0:
                possible_place = us.reset_already_placed_list(index, possible_place)
                index -= 1
            possible_place[index][2].append(board[possible_place[index][0]][possible_place[index][1]])
            board[possible_place[index][0]][possible_place[index][1]] = 0
            continue
        else:
            board[possible_place[index][0]][possible_place[index][1]] = value
            index += 1
    return board