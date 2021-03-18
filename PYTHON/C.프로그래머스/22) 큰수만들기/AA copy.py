
'''
1924
 [19, 12, 14, 92, 94, 24]  6

 4x(4-2)

'''
import itertools


def solution(number, k):
    answer = ''
    r = []
    t = [i for i in number]

    # 2개의 원소로 수열 만들기
    # print(set(list(map(''.join, itertools.permutations(t, len(t) - k)))))
    # r = set(list(map(''.join, itertools.permutations(t, len(t) - k))))

    # print(t)
    # print(len(tmp_num)) # 4
    lt = 0
    rt = k-1
    cut = k-1
    while True:
        if lt > len(t)-k:
            break

        # r.append(''.join(t[:lt]) + t[rt])
        print("org lr : ", lt)
        print("lt : %s / rt : %s " % (''.join(t[lt:cut]), t[rt]))
        if rt == len(t) - 1:
            cut += 1
            lt += 1
            rt = lt + 1
        else:
            rt += 1

    # tmp.append(int(tmp_num[i] + tmp_num[j]))
    # tmp=set(tmp)

    # print(r)
    # answer = str(max(tmp))
    return answer


# print("답 : ", solution("1924", 2))  # 94
print("답 : ", solution("1231234", 3))  # 3234
# print("답 : ", solution("4177252841", 4))  # 775841

# 1231
# 1232
# 1233
# 1234
# 2312
# 2313
# 2314
# ...
# 3123
# 3234
