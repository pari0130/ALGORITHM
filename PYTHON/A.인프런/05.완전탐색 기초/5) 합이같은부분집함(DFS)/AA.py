
# 05.완전탐색 기초

'''
6개의 숫자 리스트 를 합으로 구한 뒤 두 부분집합 함이 같은지 비교해서 yes

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/5) 합이같은부분집함(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum):  # L은 lavel, D(L, sum) 과 같은 node 상태트리로 생각해야함
    print('sum : ', sum)
    # 시간복잡도를 줄이기 위해. 두 합이 같은지 비교하려면 전체 total 절반값은 넘어갈 수 없음
    if sum > total // 2:
        return
    if L == n:  # L level 이 최대값 n을 넘어갈 수 없음
        if sum == (total - sum):
            print("YES ")
            sys.exit(0)
    else:
        DFS(L + 1, sum + a[L])  # 현재 list a[L] 에 있는 값을 sum에 더할 것인지
        DFS(L+1, sum)  # 더하지 않은 값의 노드로 이동할지 선택하는 부분임


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)  # list 전체 합
    DFS(0, 0)
    print("NO")
