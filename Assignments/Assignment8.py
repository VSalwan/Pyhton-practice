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