# 글자 수
# SWEA
# 난이도 D1

t = int(input())
for tc in range(1, t+1):
    answer = 0
    pattern = set(list(input()))
    dictionary = {}
    for character in pattern:
        dictionary[character] = 0
    string = input()
    
    for character in string:
        if not character in dictionary.keys():
            continue
        dictionary[character] += 1
        answer = max(answer, dictionary[character])

    print(f'#{tc} {answer}')





