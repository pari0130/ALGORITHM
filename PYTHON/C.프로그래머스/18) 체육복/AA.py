
'''
'''


def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        print(i)
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)


print("답 : ", solution(5, [2, 4], [1, 3, 5]))  # 5
print("답 : ", solution(5, [2, 4], [3]))  # 4
print("답 : ", solution(3, [3], [1]))  # 2
print("답 : ", solution(7, [2, 3, 4, 6], [1, 2, 3]))  # 5
