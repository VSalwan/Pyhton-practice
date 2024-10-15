# ques 1 Write a program to sum all the items in a list
list1 = [11, 5, 17, 18, 23]
total = sum(list1)
print(total)

# ques 2 Write a program to multiply all the items in a list
mul=1
for i in list1:
    mul=mul*i

print(mul)

# ques 3 Write a program to get the largest number from a list
print(max(list1))

# ques 4 Write a program to get the smallest number from a list
print(min(list1))

# ques 5 Write a program to reverse all elements in a list
list2= list1.reverse()

print(list2)
#ques 6 Write a program to turn every item in a list into its square
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# ques 7 Write a program to concatenate two lists.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

# ques 8 Write a program to add new item to list after a specified item
my_list = [10, 20, 30, 40, 50]

# Specify the item after which the new item will be added
specified_item = 30
new_item = 35
if specified_item in my_list:
    index = my_list.index(specified_item)
    my_list.insert(index + 1, new_item)
print(my_list)

# ques 9 Write a program to replace list’s item with new value if found.
my_list = [10, 20, 30, 40, 50]
old_value = 30
new_value = 35
if old_value in my_list:
    index = my_list.index(old_value)
    my_list[index] = new_value
print(my_list)

# ques 10 Write a program to remove list item from given list.
my_list = [10, 20, 30, 40, 50]
item_to_remove = 30
if item_to_remove in my_list:
    my_list.remove(item_to_remove)
print(my_list)

# ques 11 Write a program to count and print the number of odd numbers in a list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt=0
for i in numbers:
    if i%2!=0:
        print(i)
        cnt=cnt+1
print(cnt)

# ques 12 Write a program to create a new list with squares of numbers from an existing list
#using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# ques 13 Write a program to remove duplicates from a list.
my_list = [1, 2, 3, 2, 4, 5, 1, 6]
unique_list = list(set(my_list))
print(unique_list)
# ques 14 Write a program to sort numbers in a list in ascending order
numbers = [5, 3, 8, 1, 2, 7, 6, 4]
numbers.sort()
print(numbers)

# ques 15 Write a program to merge two lists into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)

