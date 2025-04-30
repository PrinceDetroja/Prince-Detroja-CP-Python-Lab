def create_array(l,b,h,n):
    x=[]
    for i in range(l):
        y=[]
        for j in range(b):
            z=[]
            for k in range(h):
                z.append(n)
            y.append(z)
        x.append(y)
    return x
a=int(input("Enter length: "))
b=int(input("Enter breadth: "))
c=int(input("Enter height: "))
n=int(input("Enter value: "))
print(create_array(a,b,c,n))
