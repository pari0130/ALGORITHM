
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
str1 = dict()
str2 = dict()

for x in a:
    str1[x] = str1.get(x, 0) + 1  # map에서 get x값을 가져오고 없으면 default로 0으로 가져오는 코드

for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break

else:  # for문에 해당되는 조건이 없는 경우 for else 문을 타서 yes 됨
    print("YES")
