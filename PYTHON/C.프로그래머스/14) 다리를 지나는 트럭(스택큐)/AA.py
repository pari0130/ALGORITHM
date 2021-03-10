'''
프로그래머스 다리를 지나는 트럭 스택 큐
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
'''

'''
방밥만 생각해서 맞는지 정답 비교
'''


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length  # 건너는 다리 길이를 초기화

    # 트럭이 존재할때만 추가되므로 트럭이 없으면 다리길이는 0 이 된다.
    while len(bridge) != 0:
        time += 1
        bridge.pop(0)  # 1초가 지나날때 마다 pop 하여 현재 추가된 트럭 이동
        if truck_weights:
            # 현재 다리위의 하중 + 추가되는 트럭 <= 다리하중
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return time


# bridge_length(다리길이), weight(다리 하중), truck_weights(트럭 하중)
print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110
