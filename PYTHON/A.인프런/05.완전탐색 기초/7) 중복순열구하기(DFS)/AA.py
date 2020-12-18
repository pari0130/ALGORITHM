
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/7) 중복순열구하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L):  # 레벨


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0
    DFS(0)
