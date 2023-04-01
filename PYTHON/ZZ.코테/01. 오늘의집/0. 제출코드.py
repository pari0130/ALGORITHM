
'''
괄호 문자열 풀이
'''

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

'''
행복기간
'''
def longest_happiness(happiness):
    happy_days = 0  # 현재 구간의 happy days 개수
    unhappy_days = 0  # 현재 구간의 unhappy days 개수
    max_len = 0  # 가장 긴 happy days 구간의 길이
    left = 0  # 현재 구간의 시작 인덱스
    start_index = 0  # 가장 긴 happy days 구간의 시작 인덱스

    for right in range(len(happiness)):
        if happiness[right] > 8:  # happy day인 경우
            happy_days += 1
        else:  # unhappy day인 경우
            unhappy_days += 1

        while unhappy_days > happy_days:  # unhappy days 개수가 더 많을 경우
            if happiness[left] > 8:
                happy_days -= 1
            else:
                unhappy_days -= 1
            left += 1

        if happy_days > unhappy_days and max_len < right - left + 1:
            max_len = right - left + 1
            start_index = left

    return max_len

