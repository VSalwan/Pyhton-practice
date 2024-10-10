y=int(input("Enter the year"))
if((y % 400 == 0) or (y % 100 != 0) and(y % 4 == 0)):
    print("Leap Year")
else:
    print("Not a leap year")

#ques 2 Write a program to check whether a person is eligible for voting or not
age=int(input("Enter the age"))
if age>18:
    print("Eligible for votting")
else:
    print("Not elligible")
# ques 3 Write a program to check whether a person is senior citizen
age=int(input("Enter the age"))
if age>60:
    print("Senior Citizen")
else:
    print("Not Senior Citizen")

# ques 4 Write a program to find the lowest number out of two numbers expected from user
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if a<b:
    print("First is smaller")
elif a>b:
    print("Second us smaller")
else:
    print("both numbers are equal")

# ques 5 Write a program to find the largest number out of two numbers expected from user
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
if a<b:
    print("Second is greater")
elif a>b:
    print("First number is greater")
else:
    print("both numbers are equal")

#ques 6 Write a program to check whether a number is even or odd.
n=int(input("Enter the  number"))
if n%2==0:
    print("Number is even")
else:
    print("NUmber is odd")

# ques 7 Write a program to find the largest number out of three numbers expected from 
#user
a=int(input("Enter the first number"))
b=int(input("Enter the second number")) 
c=int(input("Enter the third number")) 
if a>b and a>c:
    print("first number is largest")
elif b>a and b>c:
    print("Second is largest")
else:
    print("Third is largest")
# ques 8 Write a program to check whether a character is vowel or not
a= input("Enter the character")
if a=='e'or a=='i' or a=='o' or a=='u'or a=='a':
    print("character is vowel")
else:
    print("Character is not vowel")

# ques 10 Write a program to check whether a temperature is boiling or not.
    t=float(input("Enter the first number"))
    if t>100:
        print("Temperature is boiling")
    else:
        print("Temperature is not boiling")
#ques 11 Write a program to accept the marks from user and display the grade accordingly
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
# ques 12 Write a program to accept the number 1 to 7 from user and display name of day like
#1 for Sunday, 2 for Monday and so on
d=int(input("Enter the number from 1 to 7"))
if d==1:
    print("MONDAY")
elif d==2:
    print("TUESDAY")
elif d==3:
    print("WEDNESDAY")
elif d==4:
    print("THURSDAY")
elif d==5:
    print("FRIDAY")
elif d==6:
    print("SATURDAY")
else:
    print("SUNDAY")
# ques 13 Write a program to check whether the triangle is isosceles , equilateral and scalene
x=int(input("Enter the first number"))
y=int(input("Enter the second number")) 
z=int(input("Enter the third number")) 
if x == y == z:
        print("Equilateral Triangle")
 
    # Check for isosceles triangle
elif x == y or y == z or z == x:
        print("Isosceles Triangle")
 
    # Otherwise scalene triangle
else:
        print("Scalene Triangle")
# ques 15 . Write a Python program to check weather Given Number is Divisible by 7 or Not
n =int(input("Enter the number"))
if n% 7==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

# ques 15. Write a program to display “Hello” if a number entered by user is a multiple of five
#,otherwise print “Bye”
n =int(input("Enter the number"))
if n% 5==0:
    print("Hello")
else:
    print("Bye")
# ques 16 Write a programe to calculate the electricity bill (acept number of unit from user) 
#acording to the following criteria: Unit price , first 100 units No Charge ,next 100 
#units Rs 5 rupees per unit , after 200 units Rs 10 rupees per unit( For Example if units 
#is 350 than total bill amount is Rs 2000).
units =int(input("Enter the number of units"))
if units<100:
    print("no charge")
elif units>100 and units<200:
    print("amount:-",5*units)
else:
    print("Amount:", units*10)




# ques 17  Write a Python program to check if a number is positive, negative, or zero.
n= int(input("Enter the number"))
if n>0:
    print("number is postive")
elif n<0:
    print("number is negative")
else:
    print("NUmber is equal to 0")
# ques 19 Write a program to accept the age of a person and check if they are a child (0-12), a 
#teenager (13-19), an adult (20-59), or a senior (60+)
age=int(input("Enter the age "))
if age>0 and age<12:
    print("child")
elif age>12 and age <19:
    print("Teenager")
elif age>20 and age<59:
    print("adult")
else:
    print("senior")

# ques 20 Write a program to check if a number entered by the user is divisible by both 3 and 5.
m=int(input("Enter the number "))
if m%3==0 and m%5==0:
    print("number is correct")
else:
    print("Number not correct")


