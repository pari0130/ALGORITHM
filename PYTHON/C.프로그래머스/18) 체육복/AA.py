
'''
'''


def solution(n, lost, reserve):
    answer = n - len(lost)
    # reserve.insert(0, 0)
    # reserve.insert(len(reserve), 0)
    print(reserve)

    for i in range(len(lost)):
        if lost[i - 1] in reserve:
            lost.remove(i)
            answer += 1
        if lost[i - 1] in reserve:
            lost.remove(i)
            answer += 1

    for i in range(len(lost)):
        if any((lost[i] + 1 in reserve) or (lost[i] - 1 in reserve)):
            print(lost[i])
            answer += 1

    return answer


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2
