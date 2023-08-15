# Name = input("FullName")
# Number = input("Mobil Number")
# YearOfBirth = input("Year Of Birth")
# YearOfBirth = int(YearOfBirth)
# CurrentYear = 2023
# age = CurrentYear - YearOfBirth
# print(Name)
# print(age)
# Number = Number.replace(Number[3:11], "*-****-***")
# print(Number.split("-"))

def print_multiplication_table(number):
    if not isinstance(number, int):
        print("wrong enter")
        return

    for i in range(1, 11):
        result = number * i
        print(f"{number}*{i} = {result}")


input_str = input("enter number ")
if input_str.isdigit():
    input_number = int(input_str)
    print_multiplication_table(input_number)
else:
    print("wrong enter")


