# ques 1  Write a program to check if a given number is even or odd
n=int(input("Enter the number"))
if(n%2==0):
    print("Number is even")
else:
    print("Number is odd")

# ques 2 . Write a program to check if a given number is a prime number
m=int(input("Enter the number "))
for i in range(1,m/2):
    if(m%i==0 ):
        print("Number is not prime")
    else:
        print("Number is prime")

# ques 3 Write a program to find the greatest of three given numbers
a=int(input("Enter the first number "))
b=int(input("Enter the  second number "))
c=int(input("Enter the third number "))
if(a>=b and a>=c):
    print("a is greatest number")
if (b>=a and b>=c):
    print("b is greatest number")
if(c>=a and c>=b):
    print("c is the greatest")

# ques4 Write a program to calculate the sum of first n natural numbers
p=int(input("Enter the value"))
tl=0
for i in range (p):
    tl+=i
print(tl)



# ques 5 Write a program to convert a given integer to a string

g=int(input("Enter the  number "))
s=str(g)
print(type(s))

# ques 6 Write a program to convert a given string to an integer
number="54"
no=int(number)
print(no)
print(type(no))

# ques 7  Write a program to convert a given floating-point number to an integer
fl=32.22
ab=int(fl)
print(ab)

# ques 8 Write a program to convert a given integer to its binary string representation
it=8
ans = format(it, 'b')
print(ans)

#ques 9 Write a program to convert a given integer to its hexadecimal string representation.
it=43
ad=hex(it)
print(ad)

#ques 10 Write a program to convert a given binary string to an integer
str2="100"
x=int(str2,2)
print(x)

#ques 11 Write a program to convert a given hexadecimal string to an integer
hex_str = "fe00"
res = int(hex_str,16)
print(res)

#ques 12 Write a program to calculate x raised to the power y
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
print(x**y)

#ques 13 Write a program to calculate the square root of a given number
import math
num=int(input("Enter the number whose square root is to be find"))
print(math.sqrt(num))

#ques 14  Write a program to calculate the absolute value of a given number
num2=int(input("Enter the number whose absolute value  is to be find"))
print(abs(num2))

# ques 15 Write a program to find the maximum value in a given list of numbers
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list1))

# ques 16  Write a program to find the minimum value in a given list of numbers
list1 = [10, 20, 4, 45, 99]
print("Smallest element is:", min(list1))

#ques 17 Write a program to calculate the sum of all elements in a given list of numbers

list1 = [10, 20, 4, 45, 99]
total=0
for ele in range(0, len(list1)):
    total = total + list1[ele]

print(total)

# ques 18 Write a program to calculate the average of all elements in a given list of numbers
list1 = [10, 20, 4, 45, 99]
total=0
for ele in range(0, len(list1)):
    total = total + list1[ele]
print(total/len(list1))