def sum_avg(*a):
    s=0
    for i in a:
        s=s+i

    avg=s/5
    return "sum =",s,"average =",avg
a=int(input("Enter marks of 1st subject: "))
b=int(input("Enter marks of 2nd subject: "))
c=int(input("Enter marks of 3rd subject: "))
d=int(input("Enter marks of 4th subject: "))
e=int(input("Enter marks of 5th subject: "))
print(sum_avg(a,b,c,d,e))
