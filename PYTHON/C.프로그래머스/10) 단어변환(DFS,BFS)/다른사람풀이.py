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
answer = 0


def check(begin, word):
    for i in range(len(begin)):
        if begin[:i] + begin[i + 1:] == word[:i] + word[i + 1:]:
            return True


def dfs(begin, target, words, cnt):
    global answer
    if begin == target:
        answer = cnt
        return
    else:
        if len(words) == 0:
            return
        for i in range(len(words)):
            if check(begin, words[i]):
                word = words[:i] + words[i + 1:]
                print(words[i + 1:])
                print(word)
                dfs(words[i], target, word, cnt + 1)


def solution(begin, target, words):
    dfs(begin, target, words, 0)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
