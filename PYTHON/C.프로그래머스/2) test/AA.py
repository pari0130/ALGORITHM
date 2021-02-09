'''

'''
seoul = ['Jane', 'Kim']


def solution(seoul):
    print(seoul[0])
    key = 'kim'
    cnt = 0
    for i in range(len(seoul)):
        cnt += 1
        if i == key:
            print(cnt)

    print(seoul)
    answer = ''
    return answer


solution(seoul)
