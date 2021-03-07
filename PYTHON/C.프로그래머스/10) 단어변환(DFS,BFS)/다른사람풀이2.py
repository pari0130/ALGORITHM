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


def solution(begin, target, words):
    result = 0
    if target not in words:
        return 0
    diff_count = compare(begin, target)
    curr = begin

    while True:
        if curr == target:
            return result
        tmp = []
        for word in words:
            # curr와 word 1 차이
            diff_curr_word = compare(curr, word)

            # word와 taget diff_count - 1 차이
            diff_word_target = compare(word, target)

            if diff_curr_word == 1 and diff_word_target <= diff_count:
                tmp.append((diff_word_target, word))

        if not tmp:
            return 0
        else:
            tmp.sort(key=lambda x: x[0])
            print(tmp)
            curr = tmp[0][1]
            diff_count = tmp[0][0]
            result += 1


def compare(word1, word2):
    words = zip(word1, word2)
    diff = len([c1 for c1, c2 in words if c1 != c2])
    return diff


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
