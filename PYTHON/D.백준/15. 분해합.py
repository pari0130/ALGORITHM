'''
https://www.acmicpc.net/problem/2231


216 = 216 + 
'''

# N = int(input())
N = 216

print(list(map(int, str(N))))

for num in range(1, N+1):
    num_list = list(map(int, str(num)))
    num_sum = num + sum(num_list)
    if num_sum == N:
        print(num)
        break
    if num == N:
        print(0)
