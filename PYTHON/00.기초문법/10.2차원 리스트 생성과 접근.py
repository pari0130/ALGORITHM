
# a = [0]*3
# print(a)

# 2차원 리스트 3개
a = [[0] * 3 for _ in range(3)]
# print(a)

# a 0행 1열 값 입력
a[0][1] = 1
# print(a)


# 1행씩 for 문 출력
# for x in a:
# print(x)


# 대괄호 없이 숫자값 만 출력
for x in a:
    for y in x:
        print(y, end=' ')
    print()
