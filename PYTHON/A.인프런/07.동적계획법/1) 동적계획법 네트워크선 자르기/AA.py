
'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/07.동적계획법/1) 동적계획법 네트워크선 자르기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 해법은 앞에 최소 2개의 방법은 수를 지정해 두고, f(n) = f(n-2) + f(n-1) 이 현재 위치의 가지수 이므로 이 방법을 가지고 돌면 됨
n = int(input())
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2
for i in range(3, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]

print(dy[n])
