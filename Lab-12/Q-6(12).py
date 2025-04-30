class Date:
    def _init_(self, day, month, year):
        self.date = [day, month, year]  

    def _str_(self):
        return f"{self.date[0]:02}-{self.date[1]:02}-{self.date[2]}"

    def _eq_(self, other):
        return self.date == other.date

date1 = Date(22, 4, 2025)
date2 = Date(22, 4, 2025)
date3 = Date(23, 4, 2025)

print("Date 1:", date1)
print("Date 2:", date2)
print("Date 3:", date3)

print("\nIs Date 1 equal to Date 2?", date1 == date2)
print("Is Date 1 equal to Date 3?", date1 == date3)