
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
AbaAeCe
baeeACA

'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/9) 아나그램(딕셔너리 해쉬)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

a = input()
b = input()
sh = dict()

for x in a:
    sh[x] = sh.get(x, 0) + 1  # map에서 get x값을 가져오고 없으면 default로 0으로 가져오는 코드

for x in b:
    # map key val 형태로 넣었던 자료에 해당하는 자료가 있으면 -1 시킬 경우 간단하게 처리가 됨
    sh[x] = sh.get(x, 0) - 1

# for x in a:
#     if sh.get(x) > 0:
#         print("NO")
#         break
for key, val in sh.items():
    if val == 1:
        print("NO")
        break
else:
    print("YES")
