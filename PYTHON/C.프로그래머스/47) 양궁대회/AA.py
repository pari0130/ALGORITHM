'''
https://school.programmers.co.kr/learn/courses/30/lessons/92342
'''


def solution(n, info):
    answer = []
    a_point = 0
    for i in info:
        a_point += i
    print(a_point)
    l_point = -2147000000

    '''
    n발 어피치 info 맞춤
    일단 어치피 맞힌 점수 count
    ** 어치피 보다 화살 을 더 많이 맞춰야 라이언이 점수 가져옴
    ** 만약 여러 경우 중 점수 차이가 큰 경우가 같은게 나왔더라도 맞힌 점수가 더 큰 list 를 return (e.g. 4점을 더 맞춘 list 라던가)
    ** 이길 경기가 없을 경우 -1
     
    화살 -씩 없어 질 떄 까지 해서 largest 변경 
    
    
    
    '''

    return answer


print("답1 : ", solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))  # [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
print("답2 : ", solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # [-1]
print("답3 : ", solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))  # [1,1,2,0,1,2,2,0,0,0,0]
print("답4 : ", solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))  # [1,1,1,1,1,1,1,1,0,0,2]
