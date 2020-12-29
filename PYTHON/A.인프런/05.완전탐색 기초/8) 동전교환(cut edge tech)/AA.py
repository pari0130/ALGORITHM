
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/8) 동전교환(cut edge tech)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum):  # 레벨
    global res
    # 누적한 크기가 구하려는 m 보다 커지면 or 현제 레벨이 구한 res 보다 크면 구할 필요가 없으므로 return
    if sum > m or L > res:
        return
    if sum == m:  # 누적한 크기와 같을 경우
        if L < res:
            res = L
    else:
        for i in range(n):  # 3 크기의 노드만큼 a list를 하나씩 증가
            DFS(L+1, sum + a[i])  # 정렬된 5, 2, 1


if __name__ == "__main__":
    n = int(input())  # 노드 넓이
    a = list(map(int, input().split()))  # 동전 리스트
    m = int(input())  # 결과값
    res = 2147000000  # 최소값이 나오면 바꾸기 위해 정수 최고값
    # 가장큰값 부터 노드를 타고 들어가기 위함, 1부터 하면 찾아가는 노드 개수가 많아 지기 때문에
    # if sum > m
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)
