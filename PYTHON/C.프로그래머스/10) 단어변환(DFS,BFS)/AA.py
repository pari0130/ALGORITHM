'''
프로그래머스 단어변환(DFS,BFS)

'''

ch = {}
answer = 0


def equals_cnt(begin, word):
    cnt = 0
    for i in begin:
        idx = 0
        for j in word:
            if idx > 0:
                break
            if i == j:
                idx += 1
                cnt += 1

    return cnt


def DFS(begin, target, words):  # level, start
    global answer
    global ch

    if begin == target:
        return

    for i in range(len(words)):
        print(equals_cnt(begin, words[i]))
        if equals_cnt(begin, words[i]) == 2:
            if words[i] in ch:
                continue
            else:
                answer += 1
                ch[words[i]]
                print(ch)
                DFS(words[i], target, words)
                ch = {}


def solution(begin, target, words):
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    DFS(begin, target, words)  # level, start
    print("answer : ", answer)
    return answer


solution("", "", "")
