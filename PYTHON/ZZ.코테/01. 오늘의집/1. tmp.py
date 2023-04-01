'''
생각정리
https://www.acmicpc.net/problem/2869



'''


def solution(s):
    # create an empty dictionary to store the frequency of each letter
    freq_dict = {}

    # count the frequency of each letter in the string
    for letter in s:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1

    # sort the letters based on their frequency and alphabetical order
    sorted_letters = sorted(freq_dict.keys(), key=lambda x: (-freq_dict[x], x))

    # create a list to store the sorted letters with duplicates
    sorted_list = []
    for letter in sorted_letters:
        sorted_list += [letter] * freq_dict[letter]

    # create the final string by joining the sorted list
    sorted_str = ''.join(sorted_list)

    return sorted_str



print("답 : ", solution("bucketplace"))
