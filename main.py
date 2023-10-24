import sys
import error_handler as er
import utils as us
import backtracking as bt
import stochastic as st


def sudopy(board: list[list[int]], possible_place: list[(int, int, list[int])], algoType) -> list[list[int]]:
    if algoType == 1:
        return bt.backtracking(board, possible_place)
    if algoType == 2:
        return st.stochastic(board, possible_place)



try:
    start_board = er.error_handling()
    possible_place = us.create_list_tuple(start_board)
    final_board = sudopy(start_board, possible_place, int(sys.argv[2]))
    for lign in final_board:
        print(lign)
except Exception as e:
    print(f"Error in the except: {e}")
    exit(84)

