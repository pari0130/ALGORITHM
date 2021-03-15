
'''
'''

# 숫자, 자리수 10, 100, 1000


def sort(n):
    return n % 10


def solution(numbers):
    answer = ''
    other = []
    other = sorted(numbers, reverse=True, key=sort)

    for i in other:
        answer += str(i)

    return answer


print("답 : ", solution([6, 10, 2]))  # "6210"
print("답 : ", solution([3, 30, 34, 5, 9]))  # "9534330"
print("답 : ", solution([9999, 3222, 3434, 5, 9]))  # "9534330"

print((123 % 100) // 10)
print((123 % 10) // 1)
print((123 % 100) // 100)

# print(423 // 100)
