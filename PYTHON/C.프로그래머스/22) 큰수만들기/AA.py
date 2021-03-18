

def solution(number, k):
    # 1. 스택 생성
    st = []

    # 2. 큰 수가 앞자리가 되게끔 스택에 저장합니다.
    for elem in number:
        # append 하기 전에 임시 list[-1] 크기보다 큰 수가 있을 경우 list[-1] 값을 pop 하여 제외
        while st and st[-1] < elem and k > 0:
            st.pop()
            k -= 1

        # 현재 elem 을 append
        st.append(elem)

    # 3. k가 남았다면 뒤에서부터 뺍니다.
    while k > 0:
        st.pop()
        k -= 1

    answer = "".join(st)
    return answer


print("답 : ", solution("1924", 2))  # 94
# print("답 : ", solution("1231234", 3))  # 3234
# print("답 : ", solution("4177252841", 4))  # 775841
