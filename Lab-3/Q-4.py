#Write a function to remove a string from another string
def remove():
    str1=input("Enter a string: ")
    str2=input("Enter string to be removed: ")
    str1=str1.replace(str2,"")
    print(str1)

remove()
