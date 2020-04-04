def resolve():
    '''
    code here
    '''
    N, M = [int(item) for item in input().split()]
    A = [int(item) for item in input().split()]
    
    cnt = 0
    A_sum = sum(A)
    for a in A:
        if 1 / (4 * M) * A_sum <= a:
            cnt += 1

    if cnt >= M:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    resolve()
