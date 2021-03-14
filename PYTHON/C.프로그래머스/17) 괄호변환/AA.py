
'''
괄호 변환

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''


def correct(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    return True


def balance(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False


def convert(s):
    ans = ''
    for i in s:
        if i == '(':
            ans += ')'
        else:
            ans += '('

    return ans


def solution(p):
    u = ''
    v = ''
    answer = ''

    # 1. 빈문자열 혹은 올바른 문자열 일 경우 현재값 return
    if correct(p):
        return p

    # 2. 두 균형잡힌 문자열 u , v
    for i in range(2, len(p)+1):
        if balance(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    # 3. u 가 올바른 문자열 일 경우 u + 재귀
    if correct(u):
        answer = u + solution(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    # 4-3. ')'를 다시 붙입니다.
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    # 4-5. 생성된 문자열을 반환합니다.
    else:
        answer = ''
        answer += '('
        answer += solution(v)
        answer += ')'
        answer += convert(u[1:-1])

    return answer


print(solution("(()())()"))  # "(()())()"
print(solution(")("))  # "()"
print(solution("()))((()"))  # "()(())()"
