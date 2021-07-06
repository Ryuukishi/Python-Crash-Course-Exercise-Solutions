message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they
# would like. Print a message about that car, such as “Let me see if I can find you
# a Subaru.”

car_message = input("What rental car would you like?")
print(f"Let me see if I can find you a {car_message.title()}.")

# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

num_people = input("How many people are in your group?")
if int(num_people) > 8:
    print("Please wait for a table.")
else:
    print("Your table is ready.")

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.
num = input("Gimme a number and I'll tell you if it's a multiple of 10 or not.")
num = int(num)
if num % 10 == 0:
    print("Your number is a multiple of 10.")
else:
    print("Your number is not a multiple of 10.")

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

while True:
    toppings = input("What toppings would you like?")

    if toppings == 'quit':
        break
    else:
        print(f"{toppings.title()} has been added to your pizza.")


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

while True:
    age = input("What's your age? \nType 'quit' to exit.")
    if age == 'quit':
        break
    else:
        if int(age) < 3:
            print("Your ticket is free.")
        elif int(age) <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

active = True
while active:
    toppings = input("What toppings would you like?")

    if toppings == 'quit':
        active = False
    else:
        print(f"{toppings.title()} has been added to your pizza.")
