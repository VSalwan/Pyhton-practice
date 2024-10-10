# ques 1 Write a program to print the first ten natural number using for loop
for i in range(1,11):
    print(i)
# ques 2 Write a program to print all the even numbers in the given range
for i in range(11):
    if i%2==0:
        print(i)
# ques 3 Write a program to calculate the sum of all numbers from one to given numbers
n= int(input("Enter till sum is to be find"))
sum=0
for i in range(n):
    sum+=i

print(sum)

# ques 4 Write a program to calculate sum of all odd numbers in the given range
n= int(input("Enter till sum is to be find"))
sum=0
for i in range(n):
    if i%2!=0:
        sum+=i

print(sum)

# ques 5 Write a program to print multiplication table of 5
for i in range(1,11):
    print(f"5 * {i}={5*i}")

# ques 6 Write a program to count the total number of digits in a number
n= int(input("Enter the number"))
while n>0:
    print(n%10)
    n=n/10

# ques 7 Write a program that accepts word from user and reverses it
name="Vishvam"
i=0
e=len(name)

# ques 8 Write a program to find the no of even and odd numbers from a series of a numbers
a=[1,2,3,4,5,6,7,12,3,4,122,23,47,2]
coe=0
coo=0
for i in a:
    if i%2==0:
        coe=coe+1
    else:
        coo=coo+1

print(coe)
print(coo)



# ques 10  Write a program to display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)

print("Loop done")

# ques 11 Write a program to display all prime numbers within a range
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))
for number in range(start, end + 1):
    if number< 2:
        print("False")
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("False") 
    print("True")
       
# ques 12 . Write a program to print the letters in a word
name="Vishvam"

for i in name:
    print(i)

# ques 13 Write a program to print all the items in the list
list=[1,2,3,4,9,8]
for i in list:
    print(i)
# ques 14 Write a program to print each word in a sentence in a new line
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)
# ques 15 Write a program to print all the items in list in reverse order
list1=[10,23,45,22,21]
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# ques 16 print fibonacci series
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
# ques 17 check if number is armstrong number
num = int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit ** 3
    temp//=10

if num==sum:
     print(num,"is an Armstrong number")
else:
      print(num,"is not an Armstrong number")
    


