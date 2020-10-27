
# 섹션 2. 코드 구현능력 기르기.pdf

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/01.코드 구현력 기르기/8) 뒤집은 소수"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10  # 받아온값의 끝에 자리수를 구하기 위해 정수는 10 승수 이기 때문에 10으로 나누면 자리값을 구할 수 있음
        res = res * 10 + t  # return 값은 while문 하나씩 돌면서 t 받아온 값에 다시 10 승수를 곱함
        x = x // 10  # while문을 돌면서 몫이 0 이상일때 까지 돈다
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:  # x는 약수다
            return False
    else:
        return True


n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
