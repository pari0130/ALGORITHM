'''
프로그래머스 단어변환(DFS,BFS)

'''

numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    return sorted(list(set([numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))])))


print(solution(numbers))
