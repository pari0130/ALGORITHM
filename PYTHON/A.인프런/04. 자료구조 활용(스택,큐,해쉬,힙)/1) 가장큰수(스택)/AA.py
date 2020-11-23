
# 04. 자료구조 활용(스택,큐,해쉬,힙)

'''
list를 돌면서 자기앞에 자기보다 작은 수가 있는지 파악 후 하나씩 입력받은 자릿수만큼 지우면서
가장 큰 수를 만들어야 한다.

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/04. 자료구조 활용(스택,큐,해쉬,힙)/1) 가장큰수(스택)"
file = "/input.txt"
sys.stdin = open(path + file, "r")

num, m = map(int, input().split())
# string 하면 list에 들어잇는 숫자를 하나씩 접근 할 수 있음 12345 -> 1, 2, 3, 4, 5
num = list(map(int, str(num)))
stack = []

print('num : ', num)

for x in num:
    print('x1 : ', x)

    # stack이 비어있지 않고 stack의 제일 마지막 자료가 x 현재보다 작을떄
    # stack이 처음에 비어 있을때는 while 밖의 .append() 부터 넣고, 비어있지 않을때 and m > 0 and stack[-1] 스택 마지막 자료가 loop x 보다 작을때 제거를 위해 .pop()
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1  # m을 작게 줄임
        print('x2 : ', x)
        print('stack : ', stack[-1])
        print('m : ', m)
    print('before : ', stack)
    stack.append(x)

print('ai-is : ', stack)

# 아래 -m slice는 위에서 pop 만드로 원하는 m 값에 충족되지 않기 떄문에 남은 값 만큼 추가로 slice를 위함
if m != 0:
    stack = stack[: - m]

print('result : ', stack)
