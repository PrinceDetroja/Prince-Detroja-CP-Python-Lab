def compute(n):
    a=0
    b=0
    for i in range(0,n):
        b=b*10+n
        a=a+b
    return(print(a))
n=int(input("Ënter a number: "))
compute(n)
