# basic Assignment of taking user inputn and printing it
#ques 1 Write a program that converts Celsius to Fahrenheit or vice versa based on user input
#using the formulae
C=int(input("Enter the value of Celcius"))
F = C * (9/5) + 32.
print(F)

#ques 2 Write a program that checks if a number entered by the user is odd or even
n=int(input("Enter the number"))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")

#ques 3 Calculate and print the simple interest based on user-provided principal amount,
#rate of interest, and time.
p=int(input("Enter the principal"))  
r=int(input("Enter the rate of interest"))
t=int(input("Enter the time"))

si=p*r*t/100
print(si)


#ques 4 Calculate the discounted price based on the original price and discount percentage
#provided by the user.
op=int(input("Enter the orignal price"))
dp=int(input("Enter the discouny percentage"))

d=op-dp*op
dpp=op-d
print(dpp)

#ques 5 . Calculate and print the volume of a cylinder given the radius and height entered by
#the user.
r=float(input("Enter the radius"))
h=float(input("Enter the height"))
v=3.14 *(r**2)*h
print(v)

#ques 6 Calculate the age of a person based on their birth year and current year
from datetime import date 
by=int(input("Enter the birth year"))
cy=date.today().year
age =cy-by
print(age)

#ques 7 Convert kilometers to miles or miles to kilometers based on user input
k=int(input("Enter the kilometers"))
m=0.62*k
print(m)

#ques 8 . Calculate and print the area of a rectangle based on user input.
l=int(input("Enter the length"))
b=int(input("Enter the breadth"))
a=l*b
print(a)