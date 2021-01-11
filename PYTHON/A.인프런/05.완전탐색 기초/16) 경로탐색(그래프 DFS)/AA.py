
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/16) 경로탐색(그래프 DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        # for x in path:
        #     print(x, end=' ')
        # print()
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                # path.append(i)
                DFS(i)
                # path.pop()
                ch[i] = 0  # DFS 실행 후에는 체크 값을 풀어줌


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]  # 그래프
    ch = [0] * (n + 1)  # 노드기록 체크용

    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1  # 행열로 이동 위치
    cnt = 0
    # path = [] # 경로 탐색 용 테스트 코드
    # path.append(1)
    ch[1] = 1
    DFS(1)
    print(cnt)
