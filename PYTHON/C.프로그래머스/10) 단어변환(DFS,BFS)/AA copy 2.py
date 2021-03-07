'''
프로그래머스 단어변환(DFS,BFS)
begin	target	words	                                    return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	        0

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
    global answer
    global ch
    global res

    if begin == target:
        print("답 begin: %s -> target: %s" % (begin, target))
        res.append(answer)
        return
    else:
        for i in range(len(words)):
            # print("eq : ", equals_cnt(begin, words[i]))
            # print("word : ", words[i])
            # print("begin : ", begin)
            # print("target : ", target)
            eqcnt = equals_cnt(begin, words[i])
            if eqcnt == 2 and ch[words[i]] == 0:
                answer += 1
                ch[words[i]] = 1
                print("answer: %d %d" % (answer, eqcnt))
                print("begin: %s -> words: %s || target: %s " %
                      (begin, words[i], target))

                DFS(words[i], target, words)
                ch[words[i]] = 0
                answer -= 1
                # ch[i] = 0


def solution(begin, target, words):
    global answer
    global ch
    global res

    res = []
    answer = 0
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    ch = {}
    for i in words:
        ch[i] = 0

    # ch = [0] * len(words)
    DFS(begin, target, words)  # level, start

    print(res)
    if not res:
        answer = 0
    else:
        answer = min(res)
    print("answer : ", answer)  # 반환 : 1

    return answer


solution("", "", "")
