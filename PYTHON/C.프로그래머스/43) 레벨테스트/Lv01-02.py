'''
https://school.programmers.co.kr/learn/courses/30/lessons/150369?language=python3
'''
import sys

a, b = map(int, input().strip().split(' '))

for i in range(b):
    start = ""
    for j in range(a):
        start += str("*")

    print(start)

print(a + b)
