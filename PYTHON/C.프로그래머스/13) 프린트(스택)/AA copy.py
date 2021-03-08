'''
프로그래머스 프린트 스택
'''


def solution2(numbers):
    return sorted(list(set([numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))])))


def sort(arr):
    brk = False
    while True:
        if brk:
            break

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i][1] < arr[j][1]:
                    arr.append(arr.pop(0))
                    break
                else:
                    brk = True

    return arr


def solution(priorities, location):
    answer = 0
    tmp = []
    tmp2 = []

    for index, value in enumerate(priorities):
        tmp.append((index, value))
    # tmp.append(tmp.pop(0))
    print(tmp)
    print(sort(tmp))
    chk = False
    for i in range(len(priorities)):
        for j in range(i, len(priorities)):
            if priorities[i] < priorities[j]:
                priorities.append(priorities.pop(0))
                chk = True

    print(priorities)

    # tmp_idx = 1
    # for index, value in tmp:
    #     if index == location:
    #         answer = tmp_idx
    #         break
    #     tmp_idx += 1

    return answer


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
