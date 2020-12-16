
# 05.완전탐색 기초

'''
전체 부분집합을 만들고 부분집함 총 합이 입력값을 넘지 않도록 해야함

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/6) 바둑이승차"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum, tsum):  # 레벨, sum
    print('sum : ', sum)
    global result
    # sum node를 밑으로 나가서 합해지는 합이고, tsum은 node 0, node1 을 지날때 마다의 모든 합
    # 합 + (전체list합 - node합) 이 현재 구해진 최대값 보다 작을 경우 node 탐색 중지
    if sum + (total - tsum) < result:
        return
    if sum > c:  # 무게제한 return
        return
    if L == n:
        if sum > result:
            result = sum  # result 를 재할당 하므로 로컬 변수가 되어서 참조가 안되므로 에러가 발생함
    else:
        DFS(L + 1, sum + a[L], tsum + a[L])  # 현재 list a[L] 에 있는 값을 sum에 더할 것인지
        DFS(L+1, sum, tsum + sum)  # 더하지 않은 값의 노드로 이동할지 선택하는 부분임


if __name__ == "__main__":
    c, n = map(int, input().split())  # c : 최대무게, n : 마리수
    a = [0] * n
    result = -2147000000  # 합의 초기값은 최소값으로 지정
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print('result : ', result)
