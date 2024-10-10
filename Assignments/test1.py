# ques 1 
age=int(input("Enter the age "))
if age>0 and age<12:
    print("child")
elif age>12 and age <19:
    print("Teenager")
elif age>20 and age<59:
    print("adult")
else:
    print("senior")

# ques 2
mon=float(input("Enter the expense of monday"))
tue=float(input("Enter the expense of tuesday"))
wed=float(input("Enter the expense of wednesday"))
thurs=float(input("Enter the expense of thursday"))
fri=float(input("Enter the expense of friday"))
sat=float(input("Enter the expense of saturday"))
sun=float(input("Enter the expense of sunday"))
te=mon+tue+wed+thurs+fri+sat
print( te)
#ques 3 
kilo=float(input("Enter the kilometers"))
miles=kilo*0.62137119
print(miles)
# ques 4
opt=input("Enter the option")
if opt=='a':
    print("Answer is correct ")
else:
    print("Answer is not correct")

# ques 5
tbill=float(int("Enter the total bill"))
bp=float(int("Enter the total bill percentage"))
tip=bp*tbill
print(tip)

# ques 6
ms=float(int("Enter the total saving"))
yr=float(int("Enter the interest rate"))
ts=ms*12*yr+ms*12
print(ts)

# ques 7


first_hour_cost = 5
additional_hour_cost = 3
hours_parked =int(input("Enter the number of hours vehicle is parked"))
if hours_parked <= 1:
    print(first_hour_cost) 
else:
    print(first_hour_cost + (hours_parked - 1) * additional_hour_cost)

# ques 8
g=int(input("Enter the marks"))

if g>90:
    print("A+")
elif g>80 and g<90:
    print("A")
elif g>70 and g<80:
    print("B+")
elif g>60 and g<70:
    print("B")
elif g>50 and g<60:
    print("C+")
elif g>40 and g<50:
    print("C")
else:
    print("Fail")

# ques 9
a=int(input("Enter the first number"))
b=int(input("Enter the second number")) 
c=int(input("Enter the third number")) 
if a>b and a>c:
    print("first number is largest")
elif b>a and b>c:
    print("Second is largest")
else:
    print("Third is largest")

# ques 10
weight=float(input("Enter the weight "))
height=float(input("Enter the height "))
bmi = weight / (height ** 2)
    
    # Categorize the BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
     category = "Overweight"
else:
    category = "Obese"

print(category)

# ques 11
principal=float(input("Enter the principal "))
rate=float(input("Enter the rate "))
time=float(input("Enter the time "))
si=principal* rate* time/100
print(si)
# ques 12

age=int(input("Enter the age"))

if age>18:
    print("eligible to vote")
else:
    print("Npt eligible to vote")
# ques 13
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")


result = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2 if num2 != 0 else "Cannot divide by zero"
}.get(operator, "Invalid operator")

print(result)

