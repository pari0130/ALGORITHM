import functools


def comparator(a, b):
    print(a, " : ", b)
    t1 = a+b
    t2 = b+a
    # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    answer = str(int(''.join(n)))
    return answer


print("답 : ", solution([6, 10, 2]))  # "6210"
print("답 : ", solution([3, 30, 34, 5, 9]))  # "9534330"
print("답 : ", solution([9999, 9998, 3434, 5, 9]))  # "9534330"
