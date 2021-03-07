'''
프로그래머스 단어변환(DFS,BFS)
begin	target	words	                                    return
"hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit",	"cog",	["hot", "dot", "dog", "lot", "log"]	        0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)


'''


def compare(begin, word):
    words = zip(begin, word)
    diff = len([c1 for c1, c2 in words if c1 != c2])
    return diff


def equals_cnt(begin, word):  # 3자리 문자를 index 별로 비교하여 1개만 틀릴경우 체크(2개가맞는경우)
    cnt = 0
    for i in range(len(begin)):
        if begin[i] == word[i]:
            cnt += 1

    return cnt


def DFS(begin, target, words):
    global answer
    global tmp_answer
    global ch
    global res

    if tmp_answer > answer:
        return

    if begin == target:
        if answer > tmp_answer:
            answer = tmp_answer
        return
    else:
        for i in range(len(words)):
            # eqcnt = equals_cnt(begin, words[i])
            eqcnt = compare(begin, words[i])
            if eqcnt == 1 and ch[words[i]] == 0:
                tmp_answer += 1  # 방문한 카운트 증가
                ch[words[i]] = 1  # 방문한 위치 체크

                DFS(words[i], target, words)  # 방문

                tmp_answer -= 1  # 방문한 위치 카운트 감소
                ch[words[i]] = 0  # 방문한 위치 초기화


def solution(begin, target, words):
    global answer
    global tmp_answer
    global ch
    global res

    res = []
    answer = 2147000000
    tmp_answer = 0
    ch = {}

    # 방문위치 체크 변수
    for i in words:
        ch[i] = 0

    DFS(begin, target, words)  # level, start

    if answer == 2147000000:
        answer = 0

    return answer


print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]))  # 4

print(solution("1234567000", "1234567899", [
      "1234567800", "1234567890", "1234567899"]))  # 3
