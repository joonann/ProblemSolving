import heapq

def solution(food_times, k): # food_times의 크기 N, 1번부터 N번까지 음식의 번호부여, k는 방송이 중단된 시간
    
    if sum(food_times) <= k: # 음식을 먹는데 필요한 시간의 합이 방송이 중단된 시간보다 작으면 모든음식을 다먹을수 있으므로
        return -1 # -1 반환
    
    q = [] # 우선순위큐 선언
    for i in range(len(food_times)): # N개의 음식만큼 반복 음식을 먹는데 걸리는 시간이 가장 적게 걸리는 음식이 먼저 나온다.
        heapq.heappush(q, (food_times[i], i + 1)) # (음식을 먹는데 걸리는 시간, 음식의 번호)
    
    time = k # 방송 중단까지 남은 시간
    prev = 0 # 직전 음식을 먹기 위해 필요한 시간
    length = len(q) # 우선순위큐의 사이즈
    while (q[0][0] - prev) * length <= time: # (큐의 루트에 있는 노드의 시간 - 직전 음식을 먹기위해 필요한 시간) * 우선순위큐의 사이즈 값이 방송 중단까지 남은 시간보다 적으면
        time -= (q[0][0] - prev) * length # 방송중단까지 남은시간 감소
        prev = q[0][0] # 직전 음식을 먹기 위해 필요한 시간 갱신
        heapq.heappop(q) # 우선순위큐의 루트에 있는 원소 팝
        length -= 1 # 우선순위큐의 사이즈 1감소
        
    # 우선순위큐에 남아있던 요소들을 음식의 번호를 기준으로 오름차순 정렬하고,
    # 방송중단까지 남은시간을 우선순위큐의 길이로 나눈 나머지 인덱스에 해당하는 음식의 번호를 반환
    return sorted(q, key=lambda x:x[1])[time % length][1]