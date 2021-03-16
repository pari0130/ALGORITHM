
'''
2*3 배열일때 지나가는 점선의 개수는
2+3 - 최대공약수 만큼의 크기가 계산된다.

'''
import math


def solution(w, h):
    return w*h - (w+h-math.gcd(w, h))


print("답 : ", solution(8, 12))  # 80
