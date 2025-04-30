lst = ['madam','Python', "malayalam", 12321]
def isPalindrome(i):
    s=str(i)
    for n in range(len(s)//2):
        if s[n]==s[len(s)-n-1]:
            return i
            continue
        else:
            break
print(list(filter(isPalindrome, lst)))