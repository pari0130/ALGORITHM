'''

'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/19) 퀵정렬"
file = "/input.txt"
sys.stdin = open(path + file, "r")

# 퀵정렬
# chkeck.html 호출 테스트 후 기본페이지


def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos - 1)
        Qsort(pos+1, rt)


if __name__ == '__main__':
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("before sort : ", end='')
    print(arr)
    Qsort(0, 9)
    print()
    print("after sort : ", end='')
    print(arr)
