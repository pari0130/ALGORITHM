
# 05.완전탐색 기초

'''
지폐의 금액 T
동전의 가지수 k
금액 pi, 개수 ni

금액 : 20
가지수 : 3

금액,개수 :
5 3
10 2
1 5

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/4) 동전 바꿔주기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):  # 동전 개수 만큼
            DFS(L+1, sum+(cv[L])*i)  # i 로 동전의 개수를 sum에 곱해줌으로써 0개 1개 2개 덧샘


if __name__ == "__main__":
    T = int(input())  # 금액
    k = int(input())  # 가지수
    cv = list()  # 동전의 금액
    cn = list()  # 동전의 개수
    for i in range(k):
        a, b = map(int, input().split())  # 금액, 개수
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)
