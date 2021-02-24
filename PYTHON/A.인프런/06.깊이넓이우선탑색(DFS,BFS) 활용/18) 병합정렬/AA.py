'''

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/18) 병합정렬"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 병합정렬


def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2  # 가운데 자리를 구해서

        Dsort(lt, mid)
        Dsort(mid + 1, rt)

        p1 = lt  # 왼쪽 끝
        p2 = mid + 1  # p1 절반은 mid +1 부터
        tmp = []
        # p1이 절반이 되거나, p2가 오른쪽 끝이 되면 모든 list 길이 체크 했으니 종료
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp+arr[p1:mid+1]

        if p2 <= rt:
            tmp = tmp + arr[p2:rt + 1]

        for i in range(len(tmp)):
            arr[lt+1] = tmp[i]


if __name__ == '__main__':
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("before sort : ", end='')
    print(arr)
    Dsort(0, 7)
    print()
    print("after sort : ", end='')
    print(arr)
