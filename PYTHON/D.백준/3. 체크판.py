'''
https://www.acmicpc.net/problem/1018

체스판

Dfs 문제로 판단됨

For 문을 돌면서
Dx dy 값을 구해 가면서 현재 위치 위치에서 x,y 값을 상 하 좌 우 값을 구해야함
현재가 b 라면 상하좌우 값은 w 여야 하고
현재가 w 라면 상하좌우 값은 b 여야 함

그 값이 아닐 경우 카운트 증가 후 그 값은 w 혹은 b 로 변경
'''
