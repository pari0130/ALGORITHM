
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
후위식 연산을 계산해서 결과를 뽑아내야함

352+*9-
3*(5+2)-9

352*72-/+
3+5*2/(7-2)
'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/4) 후위 연산(스택)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

a = input()
stack = []
res = ''

for x in a:  # 1. 후위 표기식 목록에서 하나씩 뽑아서 x 로 받아옴
    if x.isdecimal():  # 2. 숫자는 모두 stack에 담음
        stack.append(int(x))
    else:
        if x == '+':  # 3. 연산자를 만날경우 앞의 2자리 숫자를 구해서 - if문의 연산을 해준다.
            n1 = stack.pop()  # stack[-1]
            n2 = stack.pop()  # stack[-2]
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()  # stack[-1]
            n2 = stack.pop()  # stack[-2]
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()  # stack[-1]
            n2 = stack.pop()  # stack[-2]
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()  # stack[-1]
            n2 = stack.pop()  # stack[-2]
            stack.append(n2 / n1)

print(stack[0])
