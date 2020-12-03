
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
CBA
3
CBDAGE
FGCDAB
CTSBDEA

#1 YES
#2 NO
#3 YES

1. CBA가 들어오면 CBA를 모두 들어야 함
2. CBA 순서대로 들어야 YES 아니면 NO
'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/7) 교육과정설계(큐)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)  # 입력된 CBA를 큐에 입력
    for x in plan:  # 과목 하나하나 접근
        if x in dq:  # 수업과목이 맞는지
            if x != dq.popleft():  # 큐에 담겨있는 CBA 순서에 맞는지 하나씩 꺼내서 확인.
                print('#%d no' % (i + 1))
                break
            # 위 if문의 x != dq.popleft() 로 비교만 해줘도 if문이 맞으면 dq값이 left 됨.. 신기..
            print(dq)
    else:
        if len(dq) == 0:  # 큐 CBA 값을 모두 빼서 확인 했으면 yes
            print('#%d yes' % (i + 1))
        else:
            print('#%d no' % (i + 1))
