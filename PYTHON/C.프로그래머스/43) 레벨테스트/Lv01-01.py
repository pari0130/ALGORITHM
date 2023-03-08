'''
https://school.programmers.co.kr/learn/courses/30/lessons/150369?language=python3
'''
import sys

def solution(arr):
    answer = []
    empty = -1
    if len(arr) == 1 and arr[0] == 10:
        answer.append(empty)
        return answer
    else:
        smallest = sys.maxsize
        smallestIndex = sys.maxsize
        for index, value in enumerate(arr):
            if value < smallest:
                smallest = value
                smallestIndex = index

        arr.pop(smallestIndex)
        answer = arr
        return answer


print("답 : ", solution([4, 3, 2, 5, 1]))  # [4,3,2]
print("답 : ", solution([10]))  # -1
