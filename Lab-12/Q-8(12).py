class MyString:
    def _init_(self, text):
        self.text = text

    
    def _str_(self):
        return self.text

    
    def _iadd_(self, other):
        if isinstance(other, MyString):
            self.text += other.text
        elif isinstance(other, str):
            self.text += other
        return self

    
    def toLower(self):
        self.text = self.text.lower()

    
    def toUpper(self):
        self.text = self.text.upper()


s1 = MyString("Hello")
s2 = MyString(" World")

print("Original Strings:")
print("s1:", s1)
print("s2:", s2)


s1 += s2
print("\nAfter s1 += s2:")
print("s1:", s1)

s1.toUpper()
print("\nAfter toUpper:")
print("s1:", s1)


s1.toLower()
print("\nAfter toLower:")
print("s1:", s1)