

'''


'''

import sys
from collections import deque
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/7) 송아지찾기(BFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dq = deque()
dq.append(n)
while dq:
    now = dq.popleft()
    if now == m:
        break
    # 큐 자료구조에 있는 첫번째 값을 빼서 now-1, now+1, now+5 차례대로 loop
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:
            if ch[next] == 0:
                dq.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1

print(dis[m])
