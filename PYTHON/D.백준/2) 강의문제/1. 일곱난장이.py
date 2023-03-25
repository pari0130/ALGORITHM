'''
https://www.acmicpc.net/problem/2309
'''
from itertools import *

n = []
answer = []

for i in range(9):
    n.append(int(input()))

for i in combinations(n, 7):
    if sum(i) == 100:
        answer = sorted(i)

for i in answer:
    print(i)

# 시간초과 함.....