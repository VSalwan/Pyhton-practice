# lists in python
# used to store similar or dissimilar type of data
# mutable i.e can be modified or changed
# can acces elemets through indexing
# duplicacy allowed
student_names=['Rahul','sham','Ram','Raman']
# first way to print
print(student_names)
# another way to print
for i in student_names:
    print(i)

tudos=['shopping','studing','eating','playing']
print(tudos)

# storing different data types in list
mixed=[1,'list_item',20.23,'list_item2']
print(mixed)
print(mixed[1]) # acessing element with help of index


# converting different types to list type
y="string"
z=list(y)
print(z)

# -1 give last element so on -2 second last
print(student_names[-2])

# we can also nprint range
print(student_names[1:3]) # lat element not included
print(student_names[1:-1])

# to append elements
student_names.append("shubham")
print(student_names)

# slice function 
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])

# change list items
a=['a','b','c']
a[0]='z'
print(a)

# raemove function
numbers = [2,4,7,9]
numbers.remove(2)

# len function- to calculate length of list
cars = ['BMW', 'Mercedes', 'Tesla']
print('Total Elements: ', len(cars))
