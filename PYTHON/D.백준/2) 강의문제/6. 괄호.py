'''
3. 날짜계산.py
'''
import sys

size = int(sys.stdin.readline())

for _ in range(size):
    test = str(sys.stdin.readline())
    stack = []

    for i in range(len(test)):
        if test[i] == "(":
            stack.append(test[i])
        elif test[i] == ")":
            if len(stack) > 0 and stack.count("(") > 0:
                stack.pop()
            else:
                stack.append(test[i])

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
