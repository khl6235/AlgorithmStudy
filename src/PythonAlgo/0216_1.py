# Programmers - Lv2 - Truck On Bridge
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = deque([0]*bridge_length)
    passed = 0
    on_weight = 0

    while passed < len(truck_weights):
        answer += 1
        on_weight -= on_bridge.popleft()
        if on_weight + truck_weights[passed] <= weight:
            on_bridge.append(truck_weights[passed])
            on_weight += truck_weights[passed]
            passed += 1
        else:
            on_bridge.append(0)

    return answer + bridge_length

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
bridge_length2 = 100
weight2 = 100
truck_weights2 = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length2, weight2, truck_weights2))