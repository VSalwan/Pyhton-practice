# # ques 1 Allow users to enter a password with a limited number of attempts. Use break to exit the loop upon successful entry.

# op="password"
# i=1
# while i<=5:
#     name=input("Enter the password")
#     if name==op:
#         break

# print("signed successfully")

# # ques 2 Process a list of numbers, but skip the even ones using continue
# list=[1,2,3,4,5,6,7,8,9,0]
# for i in list:
#     if i%2==0:
#         continue
#     print(i)

# # QUES 3 Create a todo list where some tasks are yet to be implemented using pass
# for x in [0, 1, 2]:
#   pass

# # QUES 4 Write a program to print numbers from 1 to 10, but stop the loop when the number is 5
# #using the break statement
# i=1
# for i in range(1,10):
#     if i==5:
#         break
#     print(i)
# # aues 5 . Write a program that keeps asking the user for a number until they enter a negative number,
# #then use break to stop the loop
# while num>=0:
#     print("Enter the number")
#     num=int(input("Enter the number"))
# #ques6 Write a program to find the first even number in a list and stop the loop using break
# list=[1,3,53,23,98,2,1,4]
# for i in list:
#     if i%2==0:
#         break
#     print(i)
# # ques 7 Write a program to print the first 5 multiples of 3, but stop if the multiple is greater than 12
# #using the break statement
#     i=1
#     while i>=0:
#         num=3*i
#         if num>12:
#             break
#         print(num)
# ques 8 Write a program to check for the presence of a specific character in a string and stop the
#loop if it is found using break
name=input("Enter the name")

for i in name:
    if i=='a':
        break
    print(i)
# ques 9 . Write a program to print numbers from 1 to 10, but skip the number 5 using the continue
#statement.
i=1
for i in range(1,10):
    if i==5:
        continue
    print(i)
# ques 10 Write a program that prints all odd numbers from 1 to 20 using the continue statement
for i in range(1,20):
    if i%2==0:
        continue
    print(i)
# ques 11 Write a program that asks the user for a series of numbers but skips the number 0 using the
#continue statement
list =[1,2,3,7,5,0,9]
for i in list:
    if i==0:
        continue
    print(i)
# ques 12 Write a program to print all the characters in a string except the vowels using the continue
#statement.
name="vishvam"
for i in name:
    if i=='a'or i=='e'or i=='i'or i=='o' or 'u':
        continue
    print(i)

# ques 13 Write a program to print all numbers from 1 to 20, but skip those divisible by 4 using the
#continue statement.
for i in range(1,20):
    if i%4==0:
        continue
    print(i)
# ques 14 . Write a program to iterate over a list and use the pass statement for all negative numbers
numbers = [5, -3, 7, -1, 0, 9, -8, 12]
for num in numbers:
    if num < 0:
        pass
    else:
        print(num)
# ques 15 Write a program that defines an empty function using the pass statement.
def my_empty_function():
    pass
my_empty_function()

# ques 16 Write a program to iterate over a string and use the pass statement for all spaces.
s="Vishvam Salwan"
for i in s:
    if i==" ":
        pass
    print(i)

# ques 17 . Write a program to create a for loop that does nothing for even numbers using the pass
#statement.
for i in range(1,20):
    if i%2==0:
        pass
    print(i)
# ques 18 Write a program to create a while loop that does nothing for numbers divisible by 3 using the
#pass statement
i=1
while i<=20:
    if i%3==0:
        pass
    print(i)
# ques 19 Write a program that prints numbers from 1 to 10, but stops if the number is 8 and skips the
#number 5
for i in range(1,10):
    if i==5:
        continue
    if i==8:
        break
# ques 20 Write a program to iterate over a list of integers, print them, but skip negative numbers and
#stop if the number 0 is encountered
list2=[1,2,3,4,-1,3,-4,0,6,7]
for i in list2:
    if i<0:
        continue
    if i==0:
        break
# ques 21 . Write a Python program that iterates over the numbers from 1 to 50. The program should:
#Skip printing any number that is divisible by 7 using the continue statement.
#Stop the loop if the number is 40 using the break statement.
#Use the pass statement for any number that is a multiple of 5 but not divisible by 2 (i.e., odd
#multiples of 5)
for i in(1,50):
    if i%7==0:
        continue
    if i%5==0 and i%2==0:
        pass
    if i==40:
        break



