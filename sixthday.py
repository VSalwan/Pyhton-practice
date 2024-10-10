# learning for loop

names=["Vishvam", "Shivam", "Rahul"]
# acessing elements of list one by one
for i in names:
    print(i)



s="Vishvam"
for si in s:
    print(si)

for i in range(10):
    print(i)

# nested loop
for i in range(2):
    for j in range(2):
        print(f"i ={i}, j={j}")
# formating
x=15
y=100
sum=x+y
print('The value of x is {} and y is {} and the sum of x and y is {}'.format(x,y, sum))