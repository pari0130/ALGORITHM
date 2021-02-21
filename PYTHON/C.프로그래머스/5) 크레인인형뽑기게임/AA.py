'''
'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/C.프로그래머스/4) 끝말잊기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    stack = []
    answer = 0
    print(board)
    print(moves)
    # 1. moves 값을 하나씩 얻어와서 board 위치 값을 stack에 append
    for i in range(len(moves)):
        move = moves[i]
        for b_list in board:
            if b_list[move-1] != 0:
                stack.append(b_list[move-1])
                b_list[move - 1] = 0
                break

        # 2. 스택 길이 1 이상일때
        while True:
            if len(stack) < 2:
                break
            if stack[-1] != stack[-2]:
                break
            else:
                answer = stack_pop(stack, answer)
                answer = stack_pop(stack, answer)

    return answer


def stack_pop(stack, answer):
    stack.pop()
    answer += 1
    return answer


solution(board, moves)
