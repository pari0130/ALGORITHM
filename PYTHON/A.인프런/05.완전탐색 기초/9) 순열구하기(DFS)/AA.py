
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/9) 순열구하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L):  # 레벨
    global cnt
    global ch
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1  # DFS가 실행 되기 전 중복을 제거하기 위해 ch list에 1로 입력
                res[L] = i
                DFS(L + 1)
                ch[i] = 0  # DFS가 실행 된 후 ch[i]에 1이 들어간 값을 초기화 시킴


if __name__ == "__main__":
    n, m = map(int, input().split())  # 3,2 (넓이, 레벨)
    res = [0] * n
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)
