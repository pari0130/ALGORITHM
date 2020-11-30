
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
1. 큐 자료구조를 생각해야함
2. 1~8 list가 있고 8번 loop를 돌면서 k=3 이라는 index를 항상 삭제 시켜서 마지막에 남는 수를 구해야함
3. k=3 이라면 k앞에 있는 0~1 index를 left 후 마지막에 append
4. k=3 을 만나면 3의 값만 popleft 시켜서 없앰
5. list를 모두 돌고 list size가 == 1 일때 print
'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/5) 공주구하기(큐)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n, k = map(int, input().split())  # 8 3
dq = list(range(1, n + 1))  # list에 1~n+1 까지 순서대로 담기 위한 list 0~7
dq = deque(dq)

print("이전 ", dq)

while dq:
    for x in range(k - 1):  # 반복문 0~1 (3-1 = 2)
        print("몇번? : ", x)
        cur = dq.popleft()  # dq에 현재 왼쪽 첫번째 값이 pop()
        print("cur : ", cur)
        dq.append(cur)  # 빼낸 값을 마지막에 append()
    dq.popleft()  # 3번 제외
    print("dq : ", dq)
    if len(dq) == 1:  # 마지막 남은 dq 일 경우
        print(dq[0])
        dq.popleft()  # 마지막 남은 자료를 마저 빼줘서 while 문 종료 or break
