def count_lower_upper(a):
    u=0
    l=0
    for i in a:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    d={"upper":u, "lower":l}
    return d

a=input("Enter a string: ")
print(count_lower_upper(a))         
