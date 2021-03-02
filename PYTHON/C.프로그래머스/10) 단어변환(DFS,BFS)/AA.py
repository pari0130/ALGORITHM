'''
프로그래머스 단어변환(DFS,BFS)

'''

from difflib import SequenceMatcher
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


str1 = 'hit'
str2 = 'ith'

ratio = SequenceMatcher(None, str1, str2).ratio()
print(ratio)
print(1 if round(SequenceMatcher(None, str1, str2).ratio(), 1) > 0.6 else 0)


# def DFS(begin, target):  # level, start
#     global answer
#     if begin == target:
#         return

#     for i in range(len(words)):
#         if words[i] in ch:

#             answer += 1


# def solution(begin, target, words):
#     # global words
#     answer = 0
#     ch = {}
#     # ch[words[0]] = 1
#     # print(ch)
#     DFS(begin, target)  # level, start
#     print(answer)
#     return answer


# print(solution(begin, target, words))
