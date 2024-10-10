#if-else sttements
number=int(input("Enter the number"))

if number>=0:
    print("Postive number")
else:
    print("Negative number")

#elif ststements
number=int(input("Enter the number"))

if number>0:
    print("Postive number")
elif number<0:
    print("Negative number")
else:
    print("Number is 0")
#nested if stetement
number=int(input("Enter the number"))
if number>0:
    if number==0:
        print("number is 0")
    else:
        print("Number is postive")

else:
    print("Number is negative")

   