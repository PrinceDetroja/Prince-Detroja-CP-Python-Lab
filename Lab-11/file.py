try:
    f = open("file", "w+")
    print(12/0)
    x = f.read()
    print(x)
except IOError:
    print("error")
except ZeroDivisionError:
    print("file doesnt exist")