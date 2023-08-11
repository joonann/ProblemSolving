# 스도쿠
# SWEA
 
sq_start = [(0, 0), (0, 3), (0, 6),\
            (3, 0), (3, 3), (3, 6),\
            (6, 0), (6, 3), (6, 6)]

def sudoku(graph):
    for i in range(9):
        row1 = set()
        sq1 = set()
        x, y = sq_start[i]
        for j in range(9):
            row1.add(graph[j][i])
            sq1.add(graph[x+j//3][y+j%3])        
        if len(set(graph[i])) != 9 or len(row1) != 9 or len(sq1) != 9:
            return 0
    return 1


t = int(input())
for tc in range(1, t+1):
    graph = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {sudoku(graph)}')