
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''

'''
import sys
import heapq as hq  # 노드 힙 구조를 사용하기 위해 heapq import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/12) 최대힙(노드)"
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
            # 출력할때도 - 부호를 추가하면 -된값이 다시 +로 되므로 최대힙 처리가 가능함
            print(-hq.heappop(a))
    else:
        # heapq는 기본이 최소 힙으로 동작하므로 - 부호를 붙혀서 최대값이 최소값으로 바뀌도록 처리함
        hq.heappush(a, -n)

# 부호를 변경하면 아래와 같은 구조가 될수 있음
# -4
# -3 - 2

# 4
# 3 2
