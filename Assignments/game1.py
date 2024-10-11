import random

print("Welcome to the Dice Game!")

# Set a target score for the player to beat
target_score = random.randint(2, 12)
print(f"Your target score to beat is: {target_score}")

# Ask player to roll the dice
input("Press Enter to roll the dice...")

# Roll two dice
die1 = random.randint(1, 6)  # Roll the first die
die2 = random.randint(1, 6)  # Roll the second die
total = die1 + die2  # Calculate the total

print(f"You rolled a {die1} and a {die2}. Total: {total}")

# Compare the total with the target score
if total > target_score:
    print("Congratulations! You beat the target score!")
elif total < target_score:
    print("Sorry, you did not beat the target score.")
else:
    print("It's a tie with the target score!")
