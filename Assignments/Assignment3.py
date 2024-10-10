#ques1 What is the result of 5 & 3 in binary and decimal?
a=5
b=3
c=a&b
print(c)  # in decimal
print(bin(c).replace("0b", "") )

#ques2 If x = 12 and y = 10, what will be the result of x & y?
x=12
y=10
print(x&y)

#ques 3  What is the result of 5 | 3 in binary and decimal?
d=a|b
print(d)
print(bin(d).replace("0b", ""))

#ques 4 If x = 6 and y = 4, what will be the result of x | y?
print(6|4)

#ques 5 What is the result of 5 ^ 3 in binary and decimal?
e=5 ^ 3
print(e)
print(bin(e).replace("0b", ""))

#ques 6 What happens when you XOR a number with itself (e.g., x ^ x)?
q=3
print(q ^q)

#ques 7 If x = 15 and y = 9, what will be the result of x ^ y?
print(15^9)

#ques 8 What is the result of ~5 in binary and decimal?
f=~5
print(f)
print(bin(f).replace("0b", ""))

#ques 9 If x = 7, what will be the result of ~x?
print(~7)

#ques 10 What is the result of shifting 8 >> 2 in binary and decimal?

g=8>>2
print(g)
print(bin(g).replace("0b", ""))

# ques 11 If x = 20, what will be the result of x >> 3?
print(20>>3)

# ques 12 What is the result of shifting 3 << 2 in binary and decimal?
h=3<<2
print(h)
print(bin(h).replace("0b", ""))

#ques 13  If x = 7, what will be the result of x << 1?
print(7<<1)

#ques 14 Can you find the result of the operation x = 12, y = 5, and calculate x | y, x & y, x ^ y, and ~x?
print(12|5)
print(12&5)
print(12 ^5)
print(~12)

#ques 15 What is the difference between the output of x << 1 and x >> 1 when x = 9?
k=2
print(k<<1)
print(k>>1)
# generaly in right shift number is multiplied by 2 and in left shift it is divide by 2

#ques 16 Using XOR (^), what is the result of 1011 ^ 1101?
print(1011 ^ 1101)
# ques 17 Given x = 29 and y = 15, calculate the result of the following operations:
# x & y
# x | y
# x ^ y
# x >> 2
# y << 3

x=29 
y=15
print(x & y)
print( x | y)
print( x ^ y)
print(x >> 2)
print(y << 3)