# ques1 Write a program to print first 10 numbers and their squares using while loop
i=1
while i<=10:
    print(i)
    print(i*i)
    i=i+1
# ques 2 Write a program to print the following series using while loop: 10, 20, 30, ………….,
#300.
d=10
while d<=300:
    print(d)
    d=d+10
# ques 3 Write a program to print first 10 natural number in reverse order using while loop.
k=10
while k>=0:
    print(k)
    k=k-1
# ques 4 Write a program to print sum of first 10 natural number using while loop
l=1
sum=0
while l<=10:
    sum+=l
    l=l+1
print(sum)

# ques 5 Write a program to print first 20 even number using while loop

e=0
c=1
while c<=20:
    print(e)
    e=e+2
    c=c+1

# ques 6 Write a program to print table of a number entered from the user using while loop
number=int(input("Enter the number"))
i=1
while i<=10:
    print(number,"*",i,'=',number*i)
    i=i+1
# ques 7 Write a program to find the average of 10 numbers using while loop.
l=1
sum=0
while l<=10:
    sum+=l
    l=l+1
print(sum/l)

# ques 8 Write a program to find the sum of even numbers using while loop
l=0
sum=0
while l<=20:
    sum+=l
    l=l+2
print(sum)
# ques 9 Write a program to print the first 10 odd numbers using a while loop
o=1
while o<=10:
    print(o)
    o+=2
# ques 10 Write a program to count the number of vowels in a string entered by the user using
#a while loop
name=input("Enter the string")
l=0
cnt=0
while l<len(name):
    if name[l]=='e'or name[l]=='i' or name[l]=='a' or name[l]=='o' or name[l]=='u':
        cnt=cnt+1
    l=l+1

# ques 11 . Write a program to calculate the factorial of a number entered by the user using a
#while loop.
i=1
n= int(input("Enter the number"))
ans=0
while i<=n:
    ans=ans*i
    i=i+1

# ques 12 Write a program to find the largest digit in a number entered by the user using a
#while loop.
nu= int(input("Enter the number"))

ln=0
while nu>=0:
    digit=nu%10
    if digit>ln:
        ln=digit
    nu//=10
print(ln)

# ques 13 Write a program to find the sum of all numbers divisible by 5 between 1 and 100
#using a while loop
l=1
s=0
while l<=100:
    if l% 5==0:
        s=s+l
    l=l+1
print(s)

#ques 14 . Write a program to count the number of digits in a number entered by the user using
#a while loop
nu= int(input("Enter the number"))

cntt=0
while nu>=0:
    digit=nu%10
    cntt=cntt+1
    nu//=10
print(cntt)

# ques 15 Write a program to keep asking the user for a number until they enter a negative
#number, then print the total sum of the entered numbers

n=int(input("Enter the number"))
sum2=0
while n>=0:
    sum2=sum2+n
    n=int(input("Enter the number"))

print(sum2)

