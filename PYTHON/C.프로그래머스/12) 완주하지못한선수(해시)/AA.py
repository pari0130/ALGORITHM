'''
프로그래머스 단어변환(DFS,BFS)

'''

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = ''
    p = {}

    for i in participant:
        if i in p:
            p[i] += 1
        else:
            p[i] = 1

    for j in completion:
        p[j] -= 1

    for key, val in p.items():
        if val == 1:
            answer = key

    return answer


print(solution(participant, completion))
