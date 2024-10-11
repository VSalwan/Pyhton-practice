# ques 1 . Write a program to check if a given number is even or odd. 
n=int(input("Enter the number"))
if n%2==0:
    print("number is even")
else:
    print("Number is odd")

# ques 2 Write a program to check if a given number is a prime number
num = int(input("Enter a number: "))
if num <= 1:
    print("Not prime")
      
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Npt prime")
        else:
           print("Prime")
# ques 3 Write a program to find the greatest of three given numbers.
a=int(input("Enter the first number"))
b=int(input("Enter the second number")) 
c=int(input("Enter the third number")) 
if a>b and a>c:
    print("first number is largest")
elif b>a and b>c:
    print("Second is largest")
else:
    print("Third is largest")
# ques 4 Write a program to calculate the sum of first n natural numbers
n= int(input("Enter till sum is to be find"))
sum=0
for i in range(n):
    sum+=i

print(sum)
# ques 5 Write a program to convert a given integer to a string
f=int(input("Enter the umber"))
g=str(f)
print(g)

# ques 6 Write a program to convert a given string to an integer
e=input("Enter the umber")
f=int(e)
print(f)
# ques 7 Write a program to convert a given floating-point number to an integer
float_number = float(input("Enter a floating-point number: "))
int_number = int(float_number)
print(int_number)

# ques 8 Write a program to convert a given integer to its binary string representation
nu = int(input("Enter an integer: "))
binary_string = bin(nu)
print(binary_string)

# ques 9 Write a program to convert a given integer to its hexadecimal string representation
num = int(input("Enter an integer: "))
hex_string = hex(num)
print(hex_string)

# ques 10 . Write a program to convert a given binary string to an integer
binary_string = input("Enter a binary string: ")
integer_value = int(binary_string, 2)
print(integer_value)

# ques 11 Write a program to convert a given hexadecimal string to an integer
hex_string = input("Enter a hexadecimal string (with or without '0x' prefix): ")
i_v = int(hex_string, 16)
print(i_v)

# ques 12  Write a program to calculate x raised to the power y
x=int(input("Enter the value of x"))
y=int(input("Enter the value of y"))
print(x**y)
# ques 13 Write a program to calculate the square root of a given number
import math
r = float(input("Enter a number: "))
square_root = math.sqrt(r)
print(square_root)

# ques 14 Write a program to calculate the absolute value of a given number
u= float(input("Enter a number: "))
absolute_value = abs(u)
print(absolute_value)

# ques 15 Write a program to find the maximum value in a given list of numbers
list1 = list(map(float, input("Enter numbers separated by spaces: ").split()))
max_value = max(list1)
print(max_value)
# ques 16 Write a program to find the minimum value in a given list of numbers
min_val=min(list1)
print(min_val)

# ques 17 Write a program to calculate the sum of all elements in a given list of numbers.
t_s=sum(list1)
print(t_s)

# ques 18 Write a program to calculate the average of all elements in a given list of numbers
l=len(list1)
avg=t_s/l
print(avg)

# ques 19 Write a program to calculate the area of a circle given its radius
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * radius ** 2
print(area)

# ques 20 Write a program to calculate the area of a rectangle given its length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(area)




