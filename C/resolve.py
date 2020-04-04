def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]

    while N >= K:
        if N >= K:
            N = N % K
        else:
            if N <= K//2:
                pass
            else:
                N = K % N
    
    if N >= K:
        N = N % K
    else:
        if N <= K//2:
            pass
        else:
            N = K % N

    print(N)

if __name__ == "__main__":
    resolve()
