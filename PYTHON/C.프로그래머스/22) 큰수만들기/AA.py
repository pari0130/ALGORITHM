
'''
2*3 배열일때 지나가는 점선의 개수는
2+3 - 최대공약수 만큼의 크기가 계산된다.

'''


def solution(number, k):
    answer = ''
    tmp = []
    tmp_num = [i for i in number]

    print(tmp_num)
    # print(len(tmp_num)) # 4
    lt = 0
    rt = k-1
    while lt < k:
        tmp.append(tmp_num[:lt] + tmp_num[rt])

        if rt == len(tmp_num)-1:
            lt += 1
            rt = lt + 1
        else:
            rt += 1

    # tmp.append(int(tmp_num[i] + tmp_num[j]))
    # tmp=set(tmp)

    print(tmp)
    # answer = str(max(tmp))
    return answer


print("답 : ", solution("1924", 2))  # 94
print("답 : ", solution("1231234", 3))  # 3234
print("답 : ", solution("4177252841", 4))  # 775841

1231
1232
1233
1234
2312
2313
2314
...
3123
3234
