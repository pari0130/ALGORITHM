
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''

후위 표기식 : 연산숫자 뒤에 연산표기를 넣어야 함
식의 순서 : 괄호, * / + - 순서
1. 숫자를 만나면 res에 담는다. 
2. 숫자가 아닌 경우 연산 우선순위를 구한한다.
2-1. ( 의 경우 무조건 먼저 넣는다
2-2. * / 의 경우 넣긴하되 둘다 우선순위가 같으니 이전의 스택 자료 중 * / 가 있으면 그 값을 가져와서 res 에 담는다
2-3. + = 의 경우에도 똑같이 넣지만 이전 스택에 여는 괄호가 없을떄 까지만 while 문을 돌면서 pop 한다
2-4. ) 닫는 괄호의 경우 똑같이 여는괄호 전까지만 pop
3. 남아있는 연산자가 있을 수 있으니 stack 이 비어있을떄 까지만 pop

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/3) 후위 표기식(스택)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

a = input()
stack = []
res = ''

for x in a:  # 중위식 탐색
    if x.isdecimal():  # 10진수 숫자인지 판별하는 함수 / 피연산자인지 확인
        res += x
    else:
        if x == '(':  # 여는 괄호는 무조건 스택에 넣는다
            stack.append(x)
        elif x == '*' or x == '/':  # 연산 우선순위 상위에 있음
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # 스택 제일 최근 자료(상단자료)
                res += stack.pop()  # 스택의 가장 상단의 자료가 * / 일 경우 출력해서 res에 누적
            stack.append(x)
        elif x == '+' or x == '-':  # 덧샘이나 뺄셈은 우선순위 하단
            while stack and stack[-1] != '(':  # 여는괄호 전까지만
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':  # 여는괄호 전까지만
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()  # 남아있는 연산자를 모두 꺼냄

print(res)
