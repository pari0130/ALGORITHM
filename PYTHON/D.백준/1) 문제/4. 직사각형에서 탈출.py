'''
https://www.acmicpc.net/problem/1085

직사각형에서 탈출

경계선 계산 

x, y, w, h = map(int, input().split()) 
print(min(x, y, w-x, h-y))

좌표 위치 x, y, 끝지점-x, 끝지점-y 중 경계선에 가장 가까운 크기를 구해야함
'''
