
'''
https://programmers.co.kr/learn/courses/30/lessons/42577

'''


'''
포인트는 가벼운사람과 무거운사람이 한 배에 타도록 계산을 해야한다.

'''


def solution2(people, limit):
    people.sort(reverse=True)
    start, end = 0, len(people)-1
    cnt = len(people)  # 전체 사람 수만큼 보트의 개수를 잡고, 두명씩 타는 경우가 생기면 -1씩 빼준다
    while start < end:  # while문 종료조건, start와 end의 인덱스가 같아지면 무게를 비교할 필요가 없다
        if people[start] + people[end] <= limit:
            end -= 1  # 두명이 같이 타는 경우가 생기면 end의 인덱스를 한칸 앞으로 변경
            cnt -= 1
        start += 1
    return cnt


def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


print("답 : ", solution([70, 50, 80, 50], 100))  # 3
print("답 : ", solution([70, 80, 50], 100))  # 3
