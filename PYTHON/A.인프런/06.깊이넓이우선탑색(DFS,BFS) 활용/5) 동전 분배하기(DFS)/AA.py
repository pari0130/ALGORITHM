
# 05.완전탐색 기초

'''


'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/5) 동전 분배하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L):
    global cnt
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            money[i] += coin[L]  # 돈을 더해서 구하고
            DFS(L + 1)  # 더한 레벨
            money[i] -= coin[L]  # 돈을 빼서 다시 구함


if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    res = 2147000000  # 차가 가장 적게 나는것을 구해야 하므로 가장 큰 값 초기화
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
