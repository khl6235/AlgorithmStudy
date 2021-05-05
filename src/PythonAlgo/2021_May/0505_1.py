# Programmers - Stack/Queue - Truck Passing Bridge
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_num = len(truck_weights)
    passed = 0
    on_weight = 0 # sum(bridge)는 시간초과
    while passed < truck_num:
        answer += 1
        on_weight -= bridge.popleft()
        if on_weight+truck_weights[0] <= weight:
            on_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
            passed += 1
        else:
            bridge.append(0)
    
    return answer + bridge_length

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length2, weight2, truck_weights2))