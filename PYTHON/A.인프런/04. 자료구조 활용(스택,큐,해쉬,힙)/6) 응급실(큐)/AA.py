
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
1. 큐 자료구조
2. 5개의 list중 2번째 대기 사람이 몇번째로 치료를 받는지 확인
3. 5개 list의 숫자는 높을수록 응급도가 위험
'''
import sys
from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/6) 응급실(큐)"
file = "/input.txt"
sys.stdin = open(path + file, "r")
