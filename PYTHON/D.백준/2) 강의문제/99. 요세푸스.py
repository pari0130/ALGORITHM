'''
https://www.acmicpc.net/problem/1158
'''

n, k = map(int, input().split())  # N과 K를 입력받음

arr = [i for i in range(1, n + 1)]  # 1부터 N까지의 숫자로 이루어진 배열을 생성

result = []  # 제거된 숫자들을 기록할 배열

num = 0  # 제거할 사람의 인덱스를 나타내는 변수

while arr:
    num = (num + k - 1) % len(arr)  # 다음에 제거할 사람의 인덱스 계산
    print(num)
    result.append(str(arr.pop(num)))  # 제거된 사람을 result 배열에 기록

print("<" + ", ".join(result) + ">")  # 요세푸스 순열 출력
