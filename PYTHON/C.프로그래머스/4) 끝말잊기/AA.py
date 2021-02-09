'''

입출력 예
n	words	result
3	[tank, kick, know, wheel, land, dream, mother, robot, tank]	[3,3]
5	[hello, observe, effect, take, either, recognize, encourage, ensure,
    establish, hang, gather, refer, reference, estimate, executive]	[0,0]
2	[hello, one, even, never, now, world, draw]	[1,3]
'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/C.프로그래머스/4) 끝말잊기"
file = "/input.txt"
sys.stdin = open(path + file, "r")

n = int(input())
words = list(input().split())
m = len(words)
index = 0
chk = True

print(words[len(words):])
# 마지막 이전 마지막 문자 찾기 print(words[0][-1])


def solution(n, words):
    global chk
    # 일단 문자열 끝말잊기가 안되는지 체크
    # for i in range(m):
    #     if i > 0:
    #         if words[i][0] != words[i - 1][-1]:
    #             print("다름 : ", i)
    #             chk = False
    #         else:
    #             chk = True

    # for i in range(m):
    #     if i > 0:
    #         if words[i][0] != words[i - 1][-1]:
    #             print("다름 : ", i)
    #             chk = False
    #         else:
    #             chk = True

    # if chk == True:

    answer = []

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer


solution(n, words)
