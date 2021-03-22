
'''
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

나중을 위해 코멘트

힙큐는 heappush 할 경우 알아서 가장 작은 수 순서대로 정렬된 결과를 return 

전달받은 list 를 힙에 넣어서 힘큐로 변환 : hq.heapify(리스트))
가장 앞의 작은 수를 return : hq.heappop(리스트)
힙에 데이터를 넣는 방법 : hq.heappush(리스트, 2)

'''

import heapq as hq  # 노드 힙 구조를 사용하기 위해 heapq import


def solution(scoville, K):
    answer = 0
    n = 0
    hq.heapify(scoville)

    while scoville:
        first = hq.heappop(scoville)

        if first >= K:
            break

        if len(scoville) <= 0:
            return -1

        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second * 2)
        answer += 1

    print(scoville)

    return answer


print("답 : ", solution([1, 2, 3, 9, 10, 12], 7))  # 2
