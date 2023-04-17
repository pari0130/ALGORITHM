'''
https://www.acmicpc.net/problem/1406

에디터
L : 	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D : 	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
B : 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $ : $라는 문자를 커서 왼쪽에 추가함
단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

시간복잡도는 O(n)

'''
import sys

stack_1 = list(sys.stdin.readline().strip())
stack_2 = []
M = int(sys.stdin.readline())
N = len(stack_1)

for i in range(M):
    order = sys.stdin.readline().strip()

    if order[0] == "L" and stack_1 != []:
        stack_2.append(stack_1.pop())
    elif order[0] == "D" and stack_2 != []:
        stack_1.append(stack_2.pop())
    elif order[0] == "B" and stack_1 != []:
        stack_1.pop()
    elif order[0] == "P":
        stack_1.append(order[2])

print("".join(stack_1 + list(reversed(stack_2))))
