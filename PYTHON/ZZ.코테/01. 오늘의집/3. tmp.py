'''
생각정리
https://www.acmicpc.net/problem/2869



'''
import itertools
import re


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


def longest_happiness_period2(happiness):
    max_period = 0
    current_period = 0
    happy_days = 0
    for score in happiness:
        if score > 8:
            happy_days += 1
            current_period += 1
            if current_period > max_period and happy_days > (current_period / 2):
                max_period = current_period
        else:
            current_period = 0
            happy_days = 0
    return max_period



print(longest_happiness_period2([9, 10, 6, 0, 4, 6, 10]))  # Output: 3
print(longest_happiness_period2([6, 10, 3, 9, 4, 10, 3, 9, 3, 10, 6]))  # Output: 9
print(longest_happiness_period2([5, 3, 1, 3, 6, 4]))  # Output: 0
