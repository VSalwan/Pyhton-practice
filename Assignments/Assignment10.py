# ques 1 You are organizing a book club and want to keep track of the books to be read this month. Create a Python list named book_club that includes the following books: "1984", "To Kill a Mockingbird", "The Great Gatsby", and "Moby Dick".
books=['1984','To Kill a Mockingbird','The Great Gatsby','Moby Dick'];
for i in books:
    print(i)

# ques 2 Given the list fruits = ["apple", "banana", "cherry", "date"], write a Python statement to print the first and last fruit in the list.
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])  # first element
print(fruits[-1]) # last element

# ques 3 You have a list of your favorite movies: favorite_movies = ["Inception", "The Matrix", "Interstellar"]. Add "The Lord of the Rings" to the end of the list using the appropriate list method
favorite_movies = ["Inception", "The Matrix", "Interstellar"]
favorite_movies.append("The Lord of the Rings")
for i in favorite_movies:
    print(i)

# ques 4 Suppose you have a grocery list: grocery_list = ["milk", "jam", "bread"]. You realize you need to buy "almond milk" instead of "milk". Write the Python code to update the list accordingly.
grocery_list = ["milk", "jam", "bread"];
grocery_list[0]= "almond milk" 
for i in grocery_list:
    print(i)

# ques 5 Your to-do list for the day is todo = ["laundry", "dishes", "vacuum", "groceries"]. After completing "dishes", remove it from the list.
todo = ["laundry", "dishes", "vacuum", "groceries"]
todo.remove("laundry")
print(todo)

# ques 6 Imagine you are tracking your daily steps for a week: steps = [5000, 7000, 6500, 8000, 7500, 6000, 7200]. Write Python code to print the steps taken from the third day to the fifth day.
steps = [5000, 7000, 6500, 8000, 7500, 6000, 7200]
x=slice(1,5)
print(steps[x])