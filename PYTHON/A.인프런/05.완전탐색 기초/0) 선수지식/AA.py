
# 05.완전탐색 기초

'''
재귀함수와 스택

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/0) 선수지식"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(x):
    if x > 0:
        DFS(x - 1)  # 3까지
        print(x)


if __name__ == "__main__":
    n = int(input())
    DFS(n)  # 깊이우선탐색
