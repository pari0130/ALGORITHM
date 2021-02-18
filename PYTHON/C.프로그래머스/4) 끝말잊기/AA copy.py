'''
입출력 예
n	words	result
3	[tank, kick, know, wheel, land, dream, mother, robot, tank]	[3,3]
5	[hello, observe, effect, take, either, recognize, encourage, ensure,
    establish, hang, gather, refer, reference, estimate, executive]	[0,0]
2	[hello, one, even, never, now, world, draw]	[1,3]

출력 
정답은 [ 번호, 차례 ] 형태로 return 해주세요.
"3번째 사람이 3번째 차례에서 틀렸다"

입력 : [tank, kick, know, wheel, land, dream, mother, robot, tank]

1. list 에서 중복된 코드가 있는지 확인
1-1. 중복된 코드가 있는 경우 바로 아웃
1-2. 중복된 코드가 있는 경우 인원수 만큼 잘라서 몇번 돌았는지 체크

2. list 에서 index 마다 마지막 글자와 첫번째 글자가 맞는지 확인
2-1. 글자가 틀릴 경우 인원수 만큼 잘라서 몇번 돌았는지 체크 

3. 탈락자가 없는 경우 0, 0

마지막 이전 마지막 문자 찾기 print(words[0][-1])
# print(words[len(words) - 1])  # draw return
cnt = words.count(target)   # 정수 1이 몇개인지 찾는다. ->> count("찾을 요소")
print("%s은, %d개 있습니다. [i : %d]" % (target, cnt, i))

dict 쓸수 있을듯. key value map 형태 

'''
import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/C.프로그래머스/4) 끝말잊기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
words = list(input().split())


def solution(n, words):
    answer = [0, 0]
    count = 1  # range가 1부터 시작하므로, 1으로 설정
    for idx in range(1, len(words)):  # 1부터 시작하는 이유는 첫번째 사람의 첫 단어는 절대 틀릴 일이 없음
        word = words[idx]  # words[idx] : 언급된 단어
        count %= n  # n 번쨰 까지 돌면 다시 1이 되도록 count = count % n
        print("count : ", count)
        if (word in words[0:idx]) or (words[idx-1][-1] != word[0]):
            answer = [count + 1, idx//n + 1]
            return answer
        count += 1
    return answer


print(solution(n, words))
