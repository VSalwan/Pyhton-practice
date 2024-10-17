# ques 1 Write a program to create a tuple with different datatypes.
mixed_tupple=("riya",10,"priya",15,24.7)
print(mixed_tupple)

# ques 2 . Write a program to add an item in a tuple
no=(1,2,3,4)
# craeting new rupple as append function are not used in tupple as tupple are immutable
no=no+(5,)     
print(no)

# ques 3 Write a program to reverse a tuple.

my_tuple = (1, 2, 3, 4, 5)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)

# ques 4 Write a program to create a tuple with a single item 50
n=(50)
print(n)

# ques 5 Write a program to swap two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple1, tuple2 = tuple2, tuple1
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# ques 6 Write a program to copy a specific element from one tuple to a new tuple
original_tuple = (10, 20, 30, 40, 50)
element_to_copy = 30
new_tuple = (element_to_copy,)
print(new_tuple)
# ques 7 Write a program to count the number of occurrences of item 50 in a tuple
my_tuple = (10, 20, 50, 30, 50, 50, 40)
count_50 = my_tuple.count(50)
print(count_50)

# ques 8 Write a program to check if all the items in tuples are same
my_tuple = (50, 50, 50, 50)

# ques 9 Check if all items in the tuple are the same
all_same = all(item == my_tuple[0] for item in my_tuple)
if all_same:
    print("All items in the tuple are the same.")
else:
    print("Not all items in the tuple are the same.")
# ques 10 Write a Python program to find the repeated items of a tuple
my_tuple = (10, 20, 30, 40, 50, 20, 30, 10, 10)
repeated_items = set([item for item in my_tuple if my_tuple.count(item) > 1])
print("Repeated items:", repeated_items)

# ques 11 Write a Python program to find the length of a tuple
n=(1,2,3,4,5)
print(len(n))

# ques 12 Write a program to find the index of an item in a tuple
my_tuple = (10, 20, 30, 40, 50)
item_to_find = 30
index = my_tuple.index(item_to_find)
print(f"The index of {item_to_find} is: {index}")

# ques 13 Write a program to convert a tuple to a string
my_tuple = ('h', 'e', 'l', 'l', 'o')
my_string = ''.join(my_tuple)
print(my_string)
# ques 14 Write a program to check if an item exists in a tuple
my_tuple = (10, 20, 30, 40, 50)
item_to_check = 30
if item_to_check in my_tuple:
    print(f"{item_to_check} exists in the tuple.")
else:
    print(f"{item_to_check} does not exist in the tuple.")
# ques 15 Write a program to concatenate two tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

# ques 16 Write a program to convert a list into a tuple
my_list = [1, 2, 3, 4, 5]

# Convert the list to a tuple
my_tuple = tuple(my_list)
print(my_tuple)

# ques 17 Write a program to find the maximum and minimum value in a tuple
my_tuple = (10, 20, 30, 40, 50)
max_value = max(my_tuple)
min_value = min(my_tuple)

print("Maximum value:", max_value)
print("Minimum value:", min_value)

# ques 18 Write a program to create a tuple from given input values
input_values = input("Enter values separated by commas: ")
my_tuple = tuple(value.strip() for value in input_values.split(','))
print("Created tuple:", my_tuple)
# ques 19 . Write a program to Find the Product of All Elements in a Tuple
my_tuple = (1, 2, 3, 4, 5)
product = 1
for number in my_tuple:
    product *= number
print("Product of all elements in the tuple:", product)

# ques 20 Write a program to Find the Average of Elements in a Tuple.
my_tuple = (10, 20, 30, 40, 50)
average = sum(my_tuple) / len(my_tuple)
print("Average of elements in the tuple:", average)
