def string_length(s):
    if s == '':
        return 0
    return 1 + string_length(s[1:])

print("Length of string:", string_length("Recursion"))