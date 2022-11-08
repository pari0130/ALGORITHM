'''
https://school.programmers.co.kr/learn/courses/30/lessons/134240?language=python3

0 배열은 항상 1, 물
1,2,3 배열이 음식, 1번배열 3개 음식 2명이서 1개씩
[1, 3, 4, 6]	"1223330333221"
[1, 7, 1, 2]	"111303111"

배열 값 받아서 1보다 클떄 까지 index + 1 값으로 insert
e.g.
3의 경우 3//2 하면 몫이 1 이므로, index 1의 값은 1
4의 경우 4//2 하면 몫이 2 이므로, index 2의 값은 배열 길이 2만큼 2, 2
6의 경우 6//2 하면 몫이 3 이므로, index 3의 값은 배열 길이 3만큼 3, 3, 3

더 이상 없으면, 0 넣고, 그동안 값 리버스, 후 insert

씩 하면서 2, 2,

'''


def solution(food):
    tmp_arr = []
    for i in range(1, len(food)):
        c = food[i] // 2
        if c > 0:
            for j in range(c):
                tmp_arr.append(str(i))
    return ''.join(tmp_arr) + "0" + ''.join(list(reversed(tmp_arr)))


print("답 : ", solution([1, 3, 4, 6]))  # "1223330333221"
print("답 : ", solution([1, 7, 1, 2]))  # "111303111"
