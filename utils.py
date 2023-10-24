import checker as ch


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
