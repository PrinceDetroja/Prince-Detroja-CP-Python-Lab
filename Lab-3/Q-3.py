#Accept 2 strings and check if one string is there in another or not
def check():
    str1=input("Enter 1st string: ")
    str2=input("Enter 2nd string: ")
    if(str1 in str2):
        print("1st string is in 2nd string")
    elif(str2 in str1):
        print("2nd string is in 1st string")
    else:
        print("No common string is present")

check()
    
    
