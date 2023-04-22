def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 피벗 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 원소로 이루어진 리스트
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 원소로 이루어진 리스트
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 원소로 이루어진 리스트

    return quicksort(left) + middle + quicksort(right)  # 재귀 호출과 리스트 병합


print(quicksort([1, 5, 2, 3, 33123, 55, 99945, 41213, 415, 8835, 12314, 4512, 78, 9, 90, 1231, 2, 123123, 5, 5, 4, ]))
