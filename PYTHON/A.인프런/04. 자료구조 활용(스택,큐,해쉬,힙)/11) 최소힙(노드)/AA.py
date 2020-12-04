
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
1) 자연수가 입력되면 최소힙에 입력한다.
2) 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다.
(출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램 종료한다.
'''
import sys
import heapq as hq  # 노드 힙 구조를 사용하기 위해 heapq import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/11) 최소힙(노드)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

a = []

while True:
    n = int(input())
    if n == -1:  # -1일 경우 종료
        break
    if n == 0:  # 0일 경우 입력되었던 숫자 중 최소힙을 출력
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))  # root node 출력 (최소힙을 출력하는 방법)
    else:
        hq.heappush(a, n)
