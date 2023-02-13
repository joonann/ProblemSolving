from itertools import permutations

# 순열 함수 이용한 리스트 생성

def solution(babbling):
    answer = 0
    baby_word = ["aya", "ye", "woo", "ma"]
    combinated_word = []
    
    for i in range(1, len(baby_word) + 1):
        for j in permutations(baby_word, i):
            combinated_word.append("".join(j))
            
            # 리스트 join 해서 append 
            
    for i in babbling:
        if i in combinated_word:
            answer += 1
    
    return answer
