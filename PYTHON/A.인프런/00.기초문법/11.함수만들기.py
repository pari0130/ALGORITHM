
# 함수만들기

# def add(a, b):
#     c = a + b
#     print(c)

# add(3, 2)
# add(5, 7)

# def add(a, b):
#     c = a + b
#     return c


# d = add(2, 3)

# print(d)

# 2개 값을 반환 할 수 있음
# def add(a, b):
#     c = a + b
#     d = a - b
#     return c, d

# print(add(2, 3))

# 소수찾기 전달하는 값 까지의 숫자를 돌며 확인
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=' ')
