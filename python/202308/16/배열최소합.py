# 배열최소합
# SWEA 난이도 D3

# N x N 배열 
# N 개의 숫자를 골라 합이 최소가 되도록
# 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.

# 인덱스 배열을 받아 각 줄마다 인덱스 요소들의 합을 반환하는 함수
def select_sum(nums, graph):
    total = 0
    for row, i in enumerate(nums):
        total += graph[row][i]
    return total

def dfs(depth, n, visited, nums, graph):
    global answer
    if depth == n:
        answer = min(answer, select_sum(nums, graph))
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            nums.append(i)
            dfs(depth+1, n, visited, nums, graph)
            nums.pop()
            visited[i] = False

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    

    visited = [False for _ in range(n)]
    answer = int(10e9)
    nums = []
    dfs(0, n, visited, nums, graph)
    
    print(f'#{tc} {answer}')