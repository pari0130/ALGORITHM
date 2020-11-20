
# 섹션 4. 이분탐색 and 그리디.pdf

'''
1부터 n까지 오름차순 정렬된 list를 처리한다는 것을 명심해야 한다.
a list를 돌면서 입력받은 숫자 만큼 앞에 빈공간이 존재 해야한다. 
0 1 0 3 0  일대 입력받은 숫자가 2라면 0인 공간을 2개 지나친 뒤 0 1 0 3 2 가 된다.
'''

import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/03.이분탐색&그리디/10) 역수열(그리디)"
file = "/input.txt"
sys.stdin = open(path + file, "rt")

n = int(input())  # 8
a = list(map(int, input().split()))  # 5 3 4 0 2 1 1 0
seq = [0] * n  # 0으로 입력받은 n개 까지 채우는 list

for i in range(n):  # a list를 돌기 위한 for
    for j in range(n):  # seq list에 채워저있는지 확인 하기 위한 seq for
        # 2. 줄여나가다가 0이 되어서 현재 자기자신의 값이 되는 경우 and seq[j]도 비어있는 경우에는 그 공간에 seq[j] = i+1
        if a[i] == 0 and seq[j] == 0:  # 빈공간인지 체크, a list
            print('??i ', i)
            print('??j ', j)
            seq[j] = i + 1  # 3. 빈공간을 찾게 되었을 경우 seq[5] 공간에 1의 숫자를 입력한다.
            print('seq[j] ', seq[j])
            print('seq ', seq)
            break
        elif seq[j] == 0:
            # 1. 처음 5가 들어왔을때 seq[j] 는 항상 0이며 5을 하나씩 줄여가면서 앞에 공간을 좁혀나감.
            # for 문을 돌면서 앞에 빈공간이 있는 경우를 찾기 위해 a[i]를 하나씩 줄여주는 것
            a[i] -= 1
            print('2 ', a[i])

for x in seq:
    print(x, end=' ')
