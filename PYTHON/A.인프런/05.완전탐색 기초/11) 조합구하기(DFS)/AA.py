
# 05.완전탐색 기초

'''
1. 이항계수를 이용한 풀이를 해야함

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/11) 조합구하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, s):  # level, start
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):  # 1 ~ 4 까지
            res[L] = i
            # 중복을 허용하지 않도록 1~4까지 증가하며 실행, s가 증가하니 for문안에 숫자도 증가되므로 중복이 제거됨
            DFS(L + 1, i+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (n + 1)
    cnt = 0
    DFS(0, 1)  # level, start
    print(cnt)
