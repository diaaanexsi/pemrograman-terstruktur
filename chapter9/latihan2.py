def star(n):
    space=2*n-1
    for p in range(n):
        print(('*'*(2*p+1)).center(space))

star(4)
