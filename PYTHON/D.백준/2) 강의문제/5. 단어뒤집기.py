'''
3. 날짜계산.py
'''
import sys

size = int(sys.stdin.readline())

for _ in range(size):
    words = sys.stdin.readline().split()
    word_list = []

    for i in range(len(words)):

        if len(words[i]) == 1:
            word_list.append(words[i])
        elif len(words[i]) == 2:
            word_list.append(words[i][-1] + words[i][0])
        else:
            tmp = list(words[i])
            for j in range(len(tmp) // 2):
                tmp[j], tmp[-j - 1] = tmp[-j - 1], tmp[j]
            else:
                word_list.append(''.join(tmp))

    print(' '.join(word_list))
