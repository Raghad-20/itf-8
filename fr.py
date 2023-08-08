num1 = int(input("enter number"))
num2 = int(input("enter number"))

def square_area(base):
    return base*4
def trinagle_area(base,hight):
    return 0.5*base*hight
def rectangular_area(base,hight):
    return base*hight
print(square_area(num1), trinagle_area(num1,num2), rectangular_area(num1,num2))
arae = square_area(num1)
print( "square_area is ", arae)

if arae >= 10:
    print("the arae large")
elif arae <=0:
    print("input wrong")
else:
    print(" the arae small")





# avarege =60
#
# if avarege >= 80:
#
#     print("very good")
# elif avarege >=60:
#      print("good")
# else:
#     print("hello")






