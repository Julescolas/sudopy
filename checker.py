import transformer as op


def can_i_put_the_number(number : int, line : list[int]) -> bool:
    return line.count(number) == 0


def legal_line(line: list[int]) -> bool:
    for value in line:
        if value == 0:
            continue
        if line.count(value) > 1:
            return False
    return True


def legal_square(board: list[list[int]], column_id:int, row_id:int) -> bool:
    array = []
    column_id = op.modify_id(column_id)
    row_id = op.modify_id(row_id)
    for row in range(row_id, row_id + 3):
        for column in range(column_id, column_id + 3):
            array.append(board[row][column])
    return legal_line(array)


def is_board_finish(board: list[list[int]]) -> bool:
    for row in board:
        for col in row:
            if col == 0:
                return False
    return True
