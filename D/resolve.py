def resolve():
    '''
    code here
    '''
    import collections
    K = int(input())

    memo = [[0 for _ in range(11)] for _ in range(10)]

    for i in range(10):
            memo[i][0] = 1 

    for i in range(10):
        for j in range(10):
            if  1 <= i <= 8:
                memo[i][j+1] = memo[i-1][j] + memo[i][j] + memo[i+1][j]
            if i == 9:
                memo[i][j+1] = memo[i][j] + memo[i-1][j]
            if i == 0:
                memo[i][j+1] = memo[i][j] + memo[i+1][j]
    print(memo)
if __name__ == "__main__":
    resolve()
