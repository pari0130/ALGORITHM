'''
'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/C.프로그래머스/4) 끝말잊기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
words = list(input().split())


def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]:
            return [(p % n)+1, (p//n)+1]
    else:
        return [0, 0]


print(solution(n, words))
