'''
3. 날짜계산.py
'''
import sys

size = int(input())
stack = []

for _ in range(size):
    command, num = "", None
    values = sys.stdin.readline().split()
    if len(values) < 2:
        command = values[0]
    else:
        command, num = str(values[0]), int(values[1])

    if command == "push" and num is not None:
        stack.append(num)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
