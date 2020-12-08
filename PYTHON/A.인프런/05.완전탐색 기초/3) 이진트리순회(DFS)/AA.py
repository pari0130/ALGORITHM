
# 05.완전탐색 기초

'''

1. 현재 노드 x2 하면 왼쪽노드, x2+1 하면 오른쪽노드로 이동됨
       1
    2     3
  4   5 6   7

2. 스택프레임
    3 D(4)
    2 D(3)
    1 D(2)
    0 D(1)

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/3) 이진트리순회(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(v):
    if v > 7:
        return
    else:
        # print('전위:', v, end=' ')  # 중요 >> print를 먼저 수행하고 DFS 호출하면 전위 순회
        DFS(v * 2)  # 왼쪽노드 호출
        # print('중위:', v, end=' ')  # 중요 >> print를 전위 수행 후 후위 사이에 DFS 호출하면 중위 순회
        DFS(v * 2 + 1)  # 오른쪽노드 호출
        print('후위:', v, end=' ')  # 중요 >> print를 DFS 모두 호출 후 호출하면 후위 순회


if __name__ == "__main__":
    DFS(1)
