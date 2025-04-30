import random
lst=[]
for i in range(10):
    lst.append(random.randint(-15,15))
print("List:",lst)
lst2 = map(lambda i:i**2,lst)
print("Square:",list(lst2))