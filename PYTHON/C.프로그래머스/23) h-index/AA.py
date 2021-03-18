

'''
논문의 인용횟수는 list

논문 n 편
h번 이상 인용된 논문이 h편 이상이고 
나머지 논문이 h번 이하 인용되었다면

h의 최댓값이 과학자의 h-index 

연구자의 발표 논문을 피인용수가 많은 순으로 정렬한 순위. 순위와 피인용수가 같아지거나 혹은 순위가 피인용수보다 작은 최대값이 h-index입니다.
위의 예시와 같이 순위보다 피인용수가 낮아지는 6순위의 바로 위의 5순위가 h-index 됨. 
즉, h-index가 5이며, 그 저자가 발표한 논문 중 5개의 논문이 적어도 각각 5번 인용되었다.

답 : 정렬해서 순위가 값 보다 작아지면 바로 위의 순위가 h-index 가 된다.
주의 : 배열의 마지막 값이 전체 길이보다 크거나 같을 경우 순위는 전체 길이 만큼 되며 h-index 이다.

'''


def solution(citations):
    citations = sorted(citations, reverse=True)
    answer = 0

    for index, value in enumerate(citations):
        if index == len(citations) - 1 and value >= index + 1:
            answer = len(citations)
            break

        if value < index + 1:
            answer = index
            break

    print(citations)

    return answer


print("답 : ", solution([3, 0, 6, 1, 5]))  # 3
print("답 : ", solution([5, 5, 5, 5, 5]))  # 5
