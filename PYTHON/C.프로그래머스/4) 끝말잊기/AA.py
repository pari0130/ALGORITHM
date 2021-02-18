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
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/C.프로그래머스/4) 끝말잊기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
words = list(input().split())
m = len(words)
ch = []

print("인원은 : ", n)
print("길이는 : ", m)
print("낱말은 : ", words)


def solution(n, words):
    answer = []
    tp = []
    cnt = 0
    cr = 0
    chkIdx = 0

    for i in range(m):
        if chkIdx == n:
            chkIdx = 1
        else:
            chkIdx += 1

        tp.append((chkIdx, cr, words[i]))  # 튜플 형태 매핑

    print(tp)

    # 일단 문자열 끝말잊기가 안되는지 체크
    # 1. list 에서 중복된 코드가 있는지 확인
    for i in range(m):
        target = words[i]
        if cnt == n:
            cnt = 1
        else:
            cnt += 1
        if ch.count(target) == 0:
            ch.append(target)
        else:
            print("현재 순서 : ", i + 1)
            print("번호 : ", cnt)
            num = i + 1
            answer.append(cnt)
            answer.append(num//n)
            break

    # for i in range(m):
    #     if i > 0:
    #         if words[i][0] != words[i - 1][-1]:
    #             print("다름 : ", i)
    #             chk = False
    #         else:
    #             chk = True

    # if chk == True:

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer


print(solution(n, words))
