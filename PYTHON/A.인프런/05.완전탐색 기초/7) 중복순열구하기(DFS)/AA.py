
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/7) 중복순열구하기(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L):  # 레벨
    global cnt
    # print("L2 : ", L)
    if L == m:  # 말단노드
        print('L m : ', L, m)
        for j in range(m):
            print(res[j], end=', ')
        print()
        # cnt를 지역변수로 인식하므로 선언하지 않으면 error 'local variable 'cnt' referenced before assignment'
        # 해당 레벨에 도착하면 카운트를 증가
        cnt = cnt+1
    else:
        for i in range(1, n + 1):
            res[L] = i  # 1. 넓이만큼 res 배열에 숫자를 같은 레벨의 1, 2, 3에 해당하는 부분
            print('i : ', i)
            # print('res : ', res)
            # print('L1 : ', L+1)
            DFS(L+1)  # DFS 1레벨이 n 번 호출 되도록 해야함


if __name__ == "__main__":
    n, m = map(int, input().split())  # 3,2 (넓이, 레벨)
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
