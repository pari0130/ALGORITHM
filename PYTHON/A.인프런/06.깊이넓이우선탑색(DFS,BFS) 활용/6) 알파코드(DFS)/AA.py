

'''


'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/6) 알파코드(DFS)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, P):  # L 은 코드위치, P 는 depth
    global cnt
    print(res)
    if L == n:
        cnt += 1
        for j in range(P):  # 0~P 전까지
            print(chr(res[j] + 64), end='')
        print()
    else:
        for i in range(1, 27):  # 1~26 loop
            if code[L] == i:  # 1~26을 돌면서 code의 list값이 같은지 비교
                res[P] = i
                DFS(L + 1, P + 1)
            # 두자리수, 코드값의 10의 자리 가 같은지 i//10, 코드 다음값이 i의 1의 자리와 같은지
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[P] = i
                DFS(L+2, P+1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)  # out of index error 방지용
    res = [0] * (n + 3)  # n 까지 해도 되지만 넉넉히 +3 길이의 res list
    cnt = 0
    DFS(0, 0)
    print(cnt)
