'''
https://school.programmers.co.kr/learn/courses/30/lessons/160585

'''

# 할 수 없는 게임인 경우 0, 가능한 게임의 경우 1
'''
O 가 선공이므로 3개가 완성 되면 승이 할 수 있음 == 1
X 가 먼저 3개가 만들어지면 O 의 승 이므로 비정상 == 0
'''


def check(board, mark):
    # 가로, 세로, 대각선 라인
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for i, j, m in lines:
        if board[i] == mark and board[j] == mark and board[m] == mark:
            return True

    return False


def solution(board):
    flat_board = ''.join(board)
    cnt_o = flat_board.count("O")
    cnt_x = flat_board.count("X")

    # X 가 더 많거나, O가 1개 이상 더 많은경우 return fail
    if cnt_x > cnt_o or cnt_o - cnt_x > 1:
        return 0

    win_o = check(flat_board, "O")
    win_x = check(flat_board, "X")

    if win_o and win_x:
        return 0
    if win_o and cnt_o - cnt_x != 1:
        return 0
    if win_x and cnt_o != cnt_x:
        return 0

    return 1


print("답1 : ", solution(["O.X", ".O.", "..X"]))  # 1
print("답2 : ", solution(["OOO", "...", "XXX"]))  # 0
print("답3 : ", solution(["...", ".X.", "..."]))  # 0
print("답4 : ", solution(["...", "...", "..."]))  # 1
print("답5 : ", solution(["OOX", "OXX", "O.."]))  # 0 세로 O 가 3개 count 동일
print("답6 : ", solution(["OOX", "OXX", "X.."]))  # 0 대각선 X 가 3개 거나, 짝이 안맞거나
print("답7 : ", solution(["X.X", "X.X", "X.O"]))  # 0 짝이 안맞고, 대각선 X 가 3개
print("답8 : ", solution(["...", ".X.", "..O"]))  # 1 짝이 맞음
print("답8 : ", solution(["OXO", ".OX", "OXX"]))  # 1

# def solution(board):
#     n = len(board[0])
#     cnt_all = {"O": 0, "X": 0, ".": 0}
#     cnt_row = {"O": 0, "X": 0, ".": 0}
#     cnt_column = {"O": 0, "X": 0, ".": 0}
#     cnt_left_cross = {"O": 0, "X": 0, ".": 0}
#     cnt_right_cross = {"O": 0, "X": 0, ".": 0}
#
#     for i in range(n):
#         cnt_left_cross[board[i][i]] += 1
#         cnt_right_cross[board[i][n - i - 1]] += 1
#         for j in range(n):
#             cnt_row[board[i][j]] += 1
#             cnt_all[board[i][j]] += 1
#             cnt_column[board[j][i]] += 1
#         else:
#             if cnt_column["X"] == 3 and cnt_column["O"] == 3:
#                 return 0
#             # print("end j")
#     else:
#         if (cnt_left_cross["X"] == 3 and cnt_left_cross["O"] == 3) \
#                 or (cnt_right_cross["X"] == 3 and cnt_right_cross["O"] == 3) \
#                 or (cnt_row["X"] == 3 and cnt_row["O"] == 3):
#             return 0
#         print("end i")
#
#     print(cnt_all)
#     if cnt_all["X"] == cnt_all["O"]:
#         return 1
#
#     return 0


# def solution(board):
#     n = len(board[0])
#     cnt_all = {"O": 0, "X": 0, ".": 0}
#     cnt_row = {"O": 0, "X": 0, ".": 0}
#     cnt_column = {"O": 0, "X": 0, ".": 0}
#     cnt_left_cross = {"O": 0, "X": 0, ".": 0}
#     cnt_right_cross = {"O": 0, "X": 0, ".": 0}
#
#     # for 중에 X == 3 이지만 O 가 2일때는 return 0
#     for i in range(n):
#         cnt_left_cross[board[i][i]] += 1
#         cnt_right_cross[board[i][n - i - 1]] += 1
#         if (cnt_left_cross["X"] == 3 and cnt_right_cross["O"] == 2) \
#                 or (cnt_right_cross["X"] == 3 and cnt_left_cross["O"] == 2):
#             return 0
#         for j in range(n):
#             cnt_row[board[i][j]] += 1
#             cnt_all[board[i][j]] += 1
#             cnt_column[board[j][i]] += 1
#         else:
#             if (cnt_row["X"] == 3 and cnt_row["O"] == 2) \
#                     or (cnt_column["X"] == 3 and cnt_column["O"] == 2):
#                 return 0
#     else:
#         if (cnt_left_cross["X"] == 3 and cnt_right_cross["O"] == 2) \
#                 or (cnt_right_cross["X"] == 3 and cnt_left_cross["O"] == 2):
#             return 0
#         if (cnt_row["X"] == 3 and cnt_row["O"] == 2) \
#                 or (cnt_column["X"] == 3 and cnt_column["O"] == 2):
#             return 0
#
#     print(cnt_all)
#     if cnt_all["X"] == cnt_all["O"]:
#         return 1
#
#     return 0
