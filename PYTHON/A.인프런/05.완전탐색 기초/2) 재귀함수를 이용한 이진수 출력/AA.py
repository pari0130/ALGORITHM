
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/2) 재귀함수를 이용한 이진수 출력"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(x):
    print('x1', x)
    if x == 0:  # 전달받은 10진수 값이 0이 되면 return (종료)
        return
    else:
        DFS(x // 2)  # 이진수는 10진수를 2로 나눈 몫을 계속 반복하며 저장.
        print('x2', x)
        print(x % 2, end=' ')


if __name__ == "__main__":
    n = int(input())
    DFS(n)
