'''
'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/C.프로그래머스/4) 끝말잊기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    print(board)
    print(moves)
    for i in board:
        print(i)
    answer = 0
    return answer


solution(board, moves)
