
'''
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.

'''


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def solution(array, commands):

    array.insert(0, 0)
    answer = []

    for command in commands:
        i, j, k = command

        tmp = array[i:j + 1]
        tmp = bubble_sort(tmp)
        tmp.insert(0, 0)
        answer.append(tmp[k])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [
      [2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
