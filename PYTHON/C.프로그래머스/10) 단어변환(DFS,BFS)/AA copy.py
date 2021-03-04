'''
프로그래머스 단어변환(DFS,BFS)

'''


def equals_cnt(begin, word):  # 3자리 문자를 index 별로 비교하여 1개만 틀릴경우 체크(2개가맞는경우)
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


def DFS(begin, target, words):
    if begin == target:
        return

    for i in range(len(words)):
        print(equals_cnt(begin, words[i]))
        if equals_cnt(begin, words[i]) == 2 and ch[i] == 0:
            answer += 1
            ch[i] = 1
            print(ch)
            print(answer)
            DFS(words[i], target, words)
            ch[i] = 0


def solution(begin, target, words):
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    ch = [0] * len(words)  # 순열 중복방지용
    print(ch)
    DFS(begin, target, words, ch)  # level, start
    print("answer : ", answer)

    return answer


solution("", "", "")
