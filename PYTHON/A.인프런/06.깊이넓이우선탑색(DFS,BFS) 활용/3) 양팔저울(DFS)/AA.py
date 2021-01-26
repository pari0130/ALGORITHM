
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/3) 양팔저울(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum):
    global res
    if L == n:
        if 0 < sum <= s:
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])  # 왼쪽
        DFS(L+1, sum-G[L])  # 오른쪽
        DFS(L+1, sum)  # 그대로의 값


if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s - len(res))
