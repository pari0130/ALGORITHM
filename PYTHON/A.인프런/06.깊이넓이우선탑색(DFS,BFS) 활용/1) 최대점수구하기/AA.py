
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/1) 최대점수구하기"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:  # 전달받은 점수가 n list 크기와 같을 경우
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])  # 문제 풀 경우
        DFS(L+1, sum, time)  # 그냥 지나갈 경우. 문제안품


if __name__ == "__main__":
    n, m = map(int, input().split())  # 점수, 시간
    pv = list()  # 점수 list
    pt = list()  # 시간 list
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2174000000
    DFS(0, 0, 0)
    print(res)
