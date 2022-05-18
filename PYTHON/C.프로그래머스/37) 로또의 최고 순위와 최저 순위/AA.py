'''
https://programmers.co.kr/learn/courses/30/lessons/77484

1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치

알아볼 수 없는 번호를 0

'''


def solution(lottos, win_nums):
    rank = {"6": 1, "5": 2, "4": 3, "3": 4, "2": 5, "1": 6, "0": 6}
    z_cnt = lottos.count(0)

    if z_cnt >= 6:
        answer = [1, 6]
    else:
        low = len((set(lottos) & set(win_nums)))
        high = low + z_cnt
        answer = [rank[str(high)], rank[str(low)]]

    return answer


print("답 : ", solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print("답 : ", solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print("답 : ", solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]
print("답 : ", solution([45, 4, 35, 20, 3, 9], [1, 2, 3, 4, 5, 6]))  # [5, 5]
