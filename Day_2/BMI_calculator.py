weight = float(input("Your weight (kg): "))
height = float(input("Your height (feet): "))
# convert feet to miter
height = (height/3.29) ** 2
# print BMI
# print(f'Your BMI is: {float("{:.2f}".format(weight/height))}')
print(f'Your BMI is: {round(weight/height,2)}')
#PEMDAS
# print(6+4/2-(1*2))
# print(6+-1)
# 6+4/2 - 2
# 6+2-2
# 6