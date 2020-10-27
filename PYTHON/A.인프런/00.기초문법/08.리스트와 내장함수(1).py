import random as r

b = list()
# print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

# range로 1~11 까지
b = list(range(1, 11))
# print(b)

# append 추가
a.append(6)
# print(a)

# insert 특정 index에 추가
a.insert(3, 7)
# print(a)

# pop 꺼내기
a.pop()
# print(a)

# 특정 index pop
a.pop(3)
# print(a)

# remove 특정 숫자 제거
a.remove(4)
# print(a)

# index 숫자 index 위치 확인
# print(a.index(5))

# sum max min
a = list(range(1, 11))
# print(sum(a))
# print(max(a))
# print(min(a))
# print(min(7, 5))

# 섞기
r.shuffle(a)
# print(a)

# 정렬
a.sort(reverse=True)
# print(a)
a.sort()
#  print(a)

# clear
a.clear()
print(a)
