# ques 1 Write a program to create a tuple with the names 'John', 'Sarah', and 'Michael' and print the tuple
names=('John', 'Sarah', 'Michael')
# ques 2 Write a program to print the first and last subject from the tuple subjects = ('Math', 'Science', 'History', 'English').
subjects = ('Math', 'Science', 'History', 'English')
print(subjects[0])
print(subjects[-1])
#ques 3 Write a program to try modifying the first item of the tuple cars = ('BMW', 'Tesla', 'Ford') and observe the error.
cars = ('BMW', 'Tesla', 'Ford')
# cars[0]='Alto'

# ques 4 Write a program to find the total number of items in the tuple fruits = ('apple', 'banana', 'cherry', 'orange') and print the result.
fruits = ('apple', 'banana', 'cherry', 'orange')
print(len(fruits))

# ques 5 Write a program to iterate through the tuple ice_creams = ('vanilla', 'chocolate', 'strawberry', 'mint') and print each item on a new line.
ice_creams = ('vanilla', 'chocolate', 'strawberry', 'mint')
for i in ice_creams:
    print(i)
# ques 6 Write a program to create a tuple using the tuple() constructor with the elements 'dog', 'cat', and 'rabbit'.
animals = tuple(('dog', 'cat', 'rabbit'))
print(animals)

# ques 7 Write a program to check if the item 'cake' exists in the tuple items = ('bread', 'cake', 'muffin', 'cookie').
items = ('bread', 'cake', 'muffin', 'cookie')
print('cake' in items)

# ques 8 Write a program to delete the tuple colors = ('red', 'blue', 'green').
colors = ('red', 'blue', 'green')
del colors

# ques 9 Write a program to create a tuple with a single item 'mango'.
f=('mango')

# ques 10 Write a program to create a tuple playlist that contains the song 'Shape of You' three times and print the tuple.
# songs =tuple('Shape of You','Shape of You','Shape of You')
# print(songs)
# tupple cannot have same more than one times
