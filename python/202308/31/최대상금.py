# import copy

# t = int(input())
# for tc in range(1, t+1):
#     s, n = input().split()
#     s = list(map(int, s))
#     n = int(n)
#     l = len(s)
#     sc = sorted(copy.copy(s),reverse=True)
#     print()
#     print(s)
#     if l > 1:
#         for i in range(n):
#             is_swap = False
#             for j in range(l):
#                 if s[j] != sc[j]:
#                     for k in range(l-1, -1, -1):
#                         if s[k] == sc[j]:
#                             break
#                     s[j], s[k] = s[k], s[j]
#                     print('n', i, s)
#                     is_swap = True
#                     break
#             if not is_swap:
#                 s[l-2], s[l-1] = s[l-1], s[l-2]
#                 print('n', i, s)
#     ans = ''.join(list(map(str,s)))
#     print(f'#{tc} {ans}')
# 바보같이 풀었네