def sunyeol(i, N):
    if i == N:
        print('i가', N,'가 되어서 더이상 깊이 못 들어감', end=' ')
        print('A출력', A)
        return
    else:
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            print('i:', i, 'j', j,  A, '스왑')
            sunyeol(i+1, N)
            A[i], A[j] = A[j], A[i]
            print('i:', i, 'j', j,  A, '원복')

n = int(input('n을 입력하시오'))
A = [i+1 for i in range(n)]
sunyeol(0, n)