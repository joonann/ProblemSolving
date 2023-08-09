# KMP 알고리즘

def kmp(all_string, pattern):
    table = [0 for _ in range(len(pattern))]    
    i = 0 
    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    print(table)

    # kmp
    result = []
    i = 0
    for j in range(len(all_string)):
        print(f'j : {j}   i : {i} ') #  pattern[i] : {pattern[i]}    pattern[j] : {pattern[j]}')
        while i > 0 and pattern[i] != all_string[j]:
            print(f'i가 0보다 크고 pattern[i]({pattern[i]}) != all_string[j]({all_string[j]})기 때문에 i를 {table[i-1]}로 할당해준다.')
            i = table[i - 1]
        print(f'while문 종료 후 i: {i}')

        if pattern[i] == all_string[j]:
            print(f'pattern[i]({pattern[i]}) == all_string[j]({all_string[j]}) 라서 i를 증가(i : {i+1}) ')
            i += 1
            if i == len(pattern):
                result.append(j - i + 1)
                print(f'i == len(pattern) ({len(pattern)}) j-1+1({j-1+1}) append 이후 i를 {table[i-1]}로 변경')
                i = table[i - 1]

    return result

string1 = 'aaaab'
pattern1 = 'ab' # 0 1 0 1 2 

print(kmp(string1, pattern1))

# table[i-1]를 해주는 게 의미가 있나? 그냥 0으로 바꿔도 될 것 같은데