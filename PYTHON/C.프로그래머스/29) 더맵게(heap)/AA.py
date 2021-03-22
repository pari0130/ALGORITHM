
'''
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
'''

import heapq as hq  # 노드 힙 구조를 사용하기 위해 heapq import


def scoville_list(tmp, scoville):
    for i in scoville:
        hq.heappush(tmp, i)

    return scoville


def solution(scoville, K):
    answer = 0
    tmp = []
    scoville_num = 0
    tmp = scoville_list(tmp, scoville)

    while min(tmp) > 7:
        scoville_num = tmp.pop(0) + (tmp.pop(0) * 2)
        tmp = scoville_list(tmp, scoville)

    print(tmp)

    # while True:
    #     hq.heapify(scoville)

    #     n = int(input())
    #     if n == -1:  # -1일 경우 종료
    #         break
    #     if n == 0:  # 0일 경우 입력되었던 숫자 중 최소힙을 출력
    #         if len(a) == 0:
    #             print(-1)
    #         else:
    #             print(hq.heappop(a))  # root node 출력 (최소힙을 출력하는 방법)
    #     else:
    #         hq.heappush(a, n)

    return answer


print("답 : ", solution([1, 2, 3, 9, 10, 12], 7))  # 2
