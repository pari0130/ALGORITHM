'''
https://www.acmicpc.net/problem/1966

프린트 큐

list 의 값을 enumerate 에 담아서 0, 값 / 1, 값 형태로 큐에 저장한다.

While 문을 돌면서 큐의 값을 가져오고
Any 로 큐의 값을 돌면서 현재 pop value 값이 큐의 값들 보다 하나라도 크다면
현재 값을 큐의 맨 뒤로 보내고

그렇지 않으면 카운트 증가
큐 pop 의 0 index 가 찾으려는 location 일때 return answer

asda
'''
