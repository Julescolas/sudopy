def modify_id(id:int) -> int:
    while id % 3 != 0:
        id -= 1
    return id


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
