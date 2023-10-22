import Checker as ch

def modify_id(id:int) -> int:
    while id % 3 != 0:
        id -= 1
    return id

def modify_col_or_row(row : int, col: int, value: int) -> (int, int):
    col += value
    if col > 8:
        col = 0
        row += value
    if col < 0:
        col = 9
        row += value
    return row, col

def legal_column(board: list[list[int]], column_id: int) -> bool:
    array = []
    for sublist in board:
        array.append(sublist[column_id])
    return ch.legal_line(array)

def transform_col_lign(board: list[list[int]], column_id: int) -> list[int]:
    array = []
    for sublist in board:
        array.append(sublist[column_id])
    return array

def transform_square_lign(board: list[list[int]], column_id:int, row_id:int) -> list[int]:
    array = []
    column_id = modify_id(column_id)
    row_id = modify_id(row_id)
    for row in range(row_id, row_id + 3):
        for column in range(column_id, column_id + 3):
            array.append(board[column][row])
    return array