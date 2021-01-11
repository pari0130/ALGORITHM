
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/15) 인접행렬"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n, m = map(int, input().split())  # 노드의 수, 가중치 list length 6, 9
# 0*노드수 만큼의 list를 list에 노드수 만큼 담아서 n*n 의 표 list가 만들어짐 (그래프)
g = [[0] * (n + 1) for _ in range(n + 1)]

print(g)

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c  # g a -> b로 가는 노드 체크


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=' ')
    print()
