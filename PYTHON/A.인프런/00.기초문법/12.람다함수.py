# 람다 함수

# def plus_one(x):
#     a = 2
#     print(self)
#     return x + a
# print(plus_one(1))

# def plus_two(x): return x + 2
# print(plus_two(1))

def plus_one(x):
    return x + 1


a = [1, 2, 3]
print(list(map(plus_one, a)))  # map(함수 혹은 타입, 인자)

print(list(map(lambda x: x+1, a)))  # map(함수 혹은 타입, 인자)
