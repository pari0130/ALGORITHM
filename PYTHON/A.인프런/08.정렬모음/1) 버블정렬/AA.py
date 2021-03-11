
'''

'''


def bubble_sort1(arr):  # 오름차순
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort2(arr):  # 오름차순
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort3(arr):  # 내림차순
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort1([2, 1, 3, 2]))
print(bubble_sort3([2, 1, 3, 2]))
