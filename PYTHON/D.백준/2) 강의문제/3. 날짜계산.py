'''
https://www.acmicpc.net/problem/1476
1 16 16 = 16
111 = 1
123 = 5266

2 17 17 = 17
3 18 18 = 18
4 19 19 = 19
5 20 1 = 20

15, 28, 19 가 맞춰질 떄 까지 년수를 더한다

'''
earth, sun, moon = map(int, input().split())
# 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

total = 0
e = s = m = 0
while True:
    if earth == e and sun == s and moon == m:
        print(total)
        break
    else:
        e += 1
        s += 1
        m += 1
        total += 1
        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1
