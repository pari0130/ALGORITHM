
# 섹션 2. 코드 구현능력 기르기.pdf
# input 1 n = 10개의 숫자를 입력받아서 3장을 뽑아 이것을 합한 숫자 list를 만든다.
# input 2 k = 합한 숫자 중 k 번째로 큰 수를 출력

import sys
path = "D:/ALGORITHM/ALGORITHM/PYTHON/01.코드 구현력 기르기/3) k번째 큰 수 - 3장카드"
file = "input.txt"
sys.stdin = open(path + "/" + file, "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()  # 중복제거 set - java에서도 Set 이 있음

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res)  # set 함수는 정렬 할 수 없으므로 list로 다시 변환
res.sort(reverse=True)  # 정렬 반대 reverse = True
print(res[k-1])
