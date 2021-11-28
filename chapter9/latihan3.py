def star(n):
    space=2*n-1
    for i in range(n):
        print(('*'*(2*i+1)).center(space))
def star2(n):
    space=3*n-1
    for i in range(n):
        print(('*'*(2*(n-i)-1)).center(space))
def star3(n):
    if (n%2==0):
        star(n//2)
    else:
        star(n//2 + 1)

    star2(n//2)

star3(7)
