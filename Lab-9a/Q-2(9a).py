lst1 = [1,2,3,4,5,6]
lst2 = [6,5,4,3,2,1]
s = lambda i,j: i+j
result = map(s,lst1,lst2)
print(list(result))