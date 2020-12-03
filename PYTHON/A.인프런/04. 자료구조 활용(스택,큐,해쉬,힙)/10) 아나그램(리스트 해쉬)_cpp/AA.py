
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''

'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/10) 아나그램(리스트 해쉬)_cpp"
file = "/input.txt"
sys.stdin = open(path + file, "r")

a = input()
b = input()
str1 = [0] * 52  # 알파벳 수 52개
str2 = [0] * 52
for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print("no")
        break
else:
    print("yes")
