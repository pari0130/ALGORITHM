
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
1. 큐 자료구조
2. 5개의 list중 2번째 대기 사람이 몇번째로 치료를 받는지 확인 (0번 index 부터 시작하는걸 명심하면 2 == 3 index)
3. 5개 list의 숫자는 높을수록 응급도가 위험
4. 현재 값이 list 값중 하나라도 큰게 있으면 현재값을 뺴서 마지막에 넣음
5. 그렇지 않으면 현재 값과 찾으려는 사람 index 를 비교해서 print break
'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/6) 응급실(큐)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n, m = map(int, input().split())
# list에 tuple(0, 값) 형태로 Q에 담아 주기위해 아래와 같이 정의함 => [(0, 60), (1, 50), (2, 70), (3, 80), (4, 90)]
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()  # popleft => (0, 60) / cur[0][1]
    # Q list를 x(0, 60)로 받으면서 cur[1] < x[1] ==> cur[60] < x[60~90]
    # 현재 cur[1] 60 값이 Q list의 숫자를 돌면서 하나라도 x[1] 60~90 보다 작은지 찾아서 작으면 마지막에 append()
    print('b : ', cur[1])
    if any(cur[1] < x[1] for x in Q):
        print('a ', cur[1])
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:  # m번째 진료받는 사람일 경우 while 종료
            break

print(cnt)
