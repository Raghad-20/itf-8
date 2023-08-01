Name = input("FullName")
Number = input("Mobil Number")
YearOfBirth = input("Year Of Birth")
YearOfBirth = int(YearOfBirth)
CurrentYear = 2023
age = CurrentYear - YearOfBirth
print(Name)
print(age)
Number = Number.replace(Number[3:11], "*-****-***")
print(Number.split("-"))