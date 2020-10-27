
# 섹션 2. 코드 구현능력 기르기.pdf

# arr = [5, 3, 7, 9, 5, 2, 6]
# arrMin = float("inf")  # 파이썬에서는 가장 큰값을 이렇게 지정함 혹은 초기값
# # arrMin = arr[0]  # 파이썬에서는 가장 큰값을 이렇게 지정함 혹은 초기값

# for i in range(len(arr)):
#     if arr[i] < arrMin:
#         arrMin = arr[i]
#         # 첫번째 loop 에서는 float("inf")값이 무한대 이니 무조건 0번 index 5가 들어오고.
#         # 그다음 숫자가 또 5랑 비교되어서 업데이트

# print(arrMin)


arr = [5, 3, 7, 9, 5, 2, 6]
arrMin = float("inf")  # 파이썬에서는 가장 큰값을 이렇게 지정함 혹은 초기값

for x in arr:
    if x < arrMin:
        arrMin = x
        # 첫번째 loop 에서는 float("inf")값이 무한대 이니 무조건 0번 index 5가 들어오고.
        # 그다음 숫자가 또 5랑 비교되어서 업데이트

print(arrMin)
