#assignment 1 of converting data from one format to other
# ques 1-4
#  Write a python program that takes in a student name, class, and section. It should
#  also take in five subject marks of the students and find the total mark and
#  percentage. Display a result in such a way that their name, class, section, and
#  percentage are printed


name=input("Enter the name of the student")
cl=input("Enter the class of the student")
section=input("Enter the section of the student")
sub1=int(input("Enter the marks of subject 1"))
sub2=int(input("Enter the marks of subject2"))
sub3=int(input("Enter the marks of subject3"))
sub4=int(input("Enter the marks of subject4"))
sub5=int(input("Enter the marks of subject5"))
totalmarks=sub1+sub2+sub3+sub4+sub5
per=totalmarks/500*100;
print(name)
print(cl)
print(section)
print(totalmarks)
print(per)

# ques 5
#Write a program that takes two string inputs representing whole numbers (e.g., "12" and "15"), converts them to floats, and prints the result in float form.
num1=input("Enter the num1")
num2=input("Enter the num1")
num3=int(num1)
num4=int(num2)
print(num3)
print(num4)

# ques 6
# Write a program that takes two string inputs representing decimal numbers (e.g., "12.8" and "89.5"), converts them to integers, and prints the result in integer form.
nu1=input("Enter the num1")
nu2=input("Enter the num1")
nu3=float(nu1)
nu4=float(nu2)
nu5=int(nu3)
nu6=int(nu4)
print(nu5)
print(nu6)
#ques 7 & 8
#Write a program that takes one integer (e.g., "67") and one float (e.g., "45.9") as inputs, converts both to float, adds them and multiply them, and prints the result.
n1=int(input("Enter the num1"))
n2=float(input("Enter the num2"))
n3=float(n1);
n4=n1+n3
n5=n1*n3
print(n4)
print(n5)
#ques 9
#Write a program that calculates the area of a triangle using base and height provided by the user (Area = 0.5 * base * height)
base=float(input("Enter the base of triangle"))
height=float(input("Enter the height of triangle"))
area=0.5*base*height
print(area)
# ques 10
#Write a program that takes two numbers as input from the user, calculates their sum and difference, and prints the results in a single line using the sep parameter.
numb1=int(input("Enter the num1"))
numb2=int(input("Enter the num2"))
print("Sum & diff of two numbers is ", numb1+numb2, numb1-numb2, sep='-')


