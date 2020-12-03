
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/8) 단어찾기(해쉬)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
p = {}
for i in range(n):
    word = input()
    p[word] = 1  # key:value 형태 map을 이와 같이 처리할 수 있음.

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
