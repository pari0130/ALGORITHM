
# 05.완전탐색 기초

'''


'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/7) 중복순열구하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L):  # 레벨
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt = cnt+1  # cnt를 지역변수로 인식하므로 선언하지 않으면 error 'local variable 'cnt' referenced before assignment'
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())  # 3,2 (넓이, 레벨)
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
