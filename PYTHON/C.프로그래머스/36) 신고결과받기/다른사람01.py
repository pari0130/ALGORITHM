'''
https://programmers.co.kr/learn/courses/30/lessons/92334


1. result 는 id_list 에 대해서 신고 결과를 수신받을 횟 수
2. k 는 누적 신고 횟수 limit
3. report 는 "신고자, 신고대상"

id_list	                            report	                                                            k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	                    ["ryan con", "ryan con", "ryan con", "ryan con"]	                3	[0,0]

'''


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
# ["con", "ryan"] # ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# ["ryan con", "ryan con", "ryan con", "ryan con"] # ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

print("답 : ", solution(id_list, report, k))
# [2,1,1,0]
