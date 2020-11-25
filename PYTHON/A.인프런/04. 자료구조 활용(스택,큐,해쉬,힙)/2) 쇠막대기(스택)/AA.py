
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/2) 쇠막대기(스택)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    # 여는 가로에서는 스택에 쌓고 다음에 닫는 괄호가 나타나면 레이저 이므로 바로 -1 은 pop 후 남아있는 (( 두개의 len(list) 를 sum에 더해준다.
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == '(':
            cnt += len(stack)
        else:
            # ')' 닫는 괄호 일때는 무조건 1개의 길이 카운트를 가지니까 ')'를 찾을 필요가 없음
            cnt += 1

print(cnt)
