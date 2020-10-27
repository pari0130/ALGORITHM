import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/01.코드 구현력 기르기/1) k번째 약수"
file = "/input.txt"
# sys.stdin = open(path + file, "rt")

n, k = map(int, input().split())  # 띄워쓰기 분리해서 입력

cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:  # for문이 정상적으로 끝나면(break를 만나지 못하면) else 로 들어옴
    print(-1)
