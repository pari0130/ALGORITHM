
# 05.완전탐색 기초

'''


'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/4) 부분집합구하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1  # 사용함
        DFS(v + 1)
        ch[v] = 0  # 사용하지않음
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    DFS(1)
