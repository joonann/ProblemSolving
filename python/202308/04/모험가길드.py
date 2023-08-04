# 그리디 알고리즘 : 현재 상황에서 가장 좋아 보이는 것만 선택하는 알고리즘
# 최적의 해를 찾지는 않을 수도 있음

# N 명의 모험가
# 공포도가 x인 모험가는 x명 이상의 그룹에만 속할 수 있음

# 입력 받아오기

n = int(input())
arr = list(map(int, input().split()))
arr.sort() # 공포도 순 오름차순 정렬

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in arr:
    count += 1 # 그룹에 i 모험가 포함
    if i <= count: # 그룹이 커져 그룹 크기가 i모험가 공포도보다 낮으면
        result += 1 
        count = 0

# 공포도가 낮은 사람부터 한명씩 그룹으로 묶으며 문제 해결
