
'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
s는 길이가 1 이상, 100이하인 스트링입니다.

s	return
abcde	c
qwer	we

'''

s = 'abcde'


def solution(s):
    a = ''
    b = len(s) % 2
    c = list(s)

    if b == 1:
        a = c[len(s)//2]
    else:
        a = c[len(s)//2-1:len(s)//2+1]

    answer = ''.join(a)
    return answer


solution(s)
