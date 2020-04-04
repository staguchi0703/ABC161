def resolve():
    '''
    code here
    '''
    A, B, C = [item for item in input().split()]

    A, B = B, A
    A, C = C, A

    print(A, B, C)
if __name__ == "__main__":
    resolve()
