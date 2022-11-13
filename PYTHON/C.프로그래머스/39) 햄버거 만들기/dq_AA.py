"""
https://school.programmers.co.kr/learn/courses/30/lessons/133502

1 ≤ ingredient의 길이 ≤ 1,000,000
ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.

[야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]
과 같을 떄 빵,야채,고기,빵이면 1개, 해당 배열을 삭제 하고 다시 빵 야채 고기 빵 이면 1개 더해서 2개 임

스택에 넣고 하나식 뺐을 떄
빵을 만나면 다음 빵 까지,
만약 빵을 꺼냈는데 바로 빵이면 pass
"""


def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for j in range(4):
                s.pop()
    return cnt


print("답 : ", solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))  # 2
print("답 : ", solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))  # 0
