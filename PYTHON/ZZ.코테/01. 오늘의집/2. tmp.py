'''
생각정리
https://www.acmicpc.net/problem/2869



'''
import itertools
import re


def calculate_all_results(exp):
    # exp를 숫자와 연산자로 분리하여 리스트에 저장합니다.
    tokens = []
    n = len(exp)
    i = 0
    while i < n:
        if exp[i].isdigit():
            j = i
            while j < n and exp[j].isdigit():
                j += 1
            tokens.append(int(exp[i:j]))
            i = j
        else:
            tokens.append(exp[i])
            i += 1

    # memo[i][j] 는 tokens[i:j+1] 의 모든 가능한 결과를 저장합니다.
    memo = [[[] for _ in range(len(tokens))] for _ in range(len(tokens))]
    # 길이가 1인 식의 결과를 미리 저장합니다.
    for i in range(len(tokens)):
        if isinstance(tokens[i], int):
            memo[i][i].append(tokens[i])
    # 길이가 2 이상인 모든 식에 대해 결과를 계산합니다.
    for k in range(2, len(tokens) + 1):
        for i in range(len(tokens) - k + 1):
            j = i + k - 1
            # tokens[i:j+1] 의 결과를 계산합니다.
            for p in range(i + 1, j, 2):
                op = tokens[p]
                if op == '+':
                    left = memo[i][p - 1]
                    right = memo[p + 1][j]
                    for x in left:
                        for y in right:
                            memo[i][j].append(x + y)
                elif op == '-':
                    left = memo[i][p - 1]
                    right = memo[p + 1][j]
                    for x in left:
                        for y in right:
                            memo[i][j].append(x - y)
                elif op == '*':
                    left = memo[i][p - 1]
                    right = memo[p + 1][j]
                    for x in left:
                        for y in right:
                            memo[i][j].append(x * y)
                elif op == '/':
                    left = memo[i][p - 1]
                    right = memo[p + 1][j]
                    for x in left:
                        for y in right:
                            if y != 0:
                                memo[i][j].append(x / y)

    return sorted(memo[0][-1])


# 제출 코드 다시 확인 필수 !!
def calculate_all_results(exp):
    # exp 문자열을 받아서 모든 가능한 결과를 반환하는 함수
    def helper(exp):
        results = []
        # 문자열을 중간에서 나눠서 재귀적으로 계산
        for i in range(1, len(exp)-1):
            if exp[i] in ['+', '-', '*', '/']:
                # 연산자 기준으로 왼쪽과 오른쪽 부분식을 계산
                left = helper(exp[:i])
                right = helper(exp[i+1:])
                # 왼쪽 부분식과 오른쪽 부분식의 모든 결과를 조합하여 결과 리스트에 추가
                for l in left:
                    for r in right:
                        if exp[i] == '+':
                            res = l + r
                        elif exp[i] == '-':
                            res = l - r
                        elif exp[i] == '*':
                            res = l * r
                        else:  # exp[i] == '/'
                            # 정수 나눗셈으로 나누어 떨어지는 경우에만 결과에 추가
                            if r != 0 and l % r == 0:
                                res = l // r
                            else:
                                continue  # 부동소수점 나눗셈은 스킵
                        results.append(res)
        # 연산자가 없는 경우에는 exp 문자열이 정수인지 확인하여 결과 리스트에 추가
        if not results:
            try:
                results = [int(exp)]
            except ValueError:
                pass  # exp가 정수가 아닌 경우는 무시
        return results

    # helper 함수의 결과를 정렬하여 반환
    return sorted(helper(exp))



# Test the function
exp = "3*2-5*1"
print(calculate_all_results2(exp))  # Output: [-9, -9, -9, 1, 1]
