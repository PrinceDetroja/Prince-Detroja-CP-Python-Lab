def count():
    str=input("Enter a string: ")
    a=0
    n=0
    for i in range(0,len(str)):
        if str[i].isalpha()==True:
            a+=1
        elif str[i].isdigit() == True:
            n+=1

    print("Total number of alphabets=",a)
    print("Total number of digits=",n)


count()
            
