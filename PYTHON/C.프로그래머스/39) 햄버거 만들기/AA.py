'''
https://school.programmers.co.kr/learn/courses/30/lessons/133502

1 ≤ ingredient의 길이 ≤ 1,000,000
ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.

[야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]
과 같을 떄 빵,야채,고기,빵이면 1개, 해당 배열을 삭제 하고 다시 빵 야채 고기 빵 이면 1개 더해서 2개 임

스택에 넣고 하나식 뺐을 떄
빵을 만나면 다음 빵 까지,
만약 빵을 꺼냈는데 바로 빵이면 pass



'''

from collections import deque  # 데큐를 쓰기 위해 컬렉션에서 import


def solution(ingredient):
    answer = 0
    b = 1
    v = 2
    burger = [1, 2, 3, 1]
    burger_size = len(burger)
    b_idx_arr = [0]
    s = 0

    while True:
        if len(ingredient) == 0 or burger_size > len(ingredient) >= s + 4 or len(ingredient) <= s or len(b_idx_arr) == 0:
            break
        else:
            if ingredient[s] == b:
                store = ingredient[s:s + 4]  # 특정 위치 부터 자름 s ~ e
                if store == burger:
                    for i in range(s, s + 4):
                        if len(ingredient) < s:
                            break
                        del ingredient[s]
                    answer += 1
                    s = b_idx_arr.pop()
                else:
                    b_idx_arr.insert(0, ingredient[s])
                    s += 1
            else:
                s += 1

    print("answer : " + str(answer))

    return answer


print("답 : ", solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))  # 2
print("답 : ", solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))  # 0
