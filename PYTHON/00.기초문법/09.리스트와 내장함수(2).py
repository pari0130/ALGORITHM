a = [23, 12, 36, 53, 19]

# index 3까지 slice
# print(a[:3])
# print(a[1:4])
# print(len(a))

# for i in range(len(a)):
# print(a[i], end=' ')

# 홀수 출력
# for x in a:
#     if x % 2 == 1:
#         print(x, end=' ')

# index와 velue값 튜플 매핑
# for x in enumerate(a):
#     print(x)

# enumerate에서 index, value 뽑기
# for index, value in enumerate(a):
#     print(index, value)

# all 비교 모두가 참일때만 참을 return
# 하나라도 거짓일 경우 문제가됨
if all(60 > x for x in a):
    print("y")
else:
    print("n")

# any 하나라도 참이 있는 경우 return
if any(15 > x for x in a):
    print("y")
else:
    print("n")
