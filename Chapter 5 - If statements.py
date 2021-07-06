##5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
##variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
##• Write an if statement to test whether the alien’s color is green. If it is, print
##a message that the player just earned 5 points.

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

##• Write one version of this program that passes the if test and another that
##fails. (The version that fails will have no output.)


if alien_color == 'red':
    print("You just earned 5 points!")

##5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
##write an if-else chain.
##• If the alien’s color is green, print a statement that the player just earned
##5 points for shooting the alien.
##• If the alien’s color isn’t green, print a statement that the player just earned
##10 points.

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
if alien_color != 'green':
    print("You just earned 10 points!")

    
##• Write one version of this program that runs the if block and another that
##runs the else block.

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")


##5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
##• If the alien is green, print a message that the player earned 5 points.
##• If the alien is yellow, print a message that the player earned 10 points.
##• If the alien is red, print a message that the player earned 15 points.
##• Write three versions of this program, making sure each message is printed
##for the appropriate color alien.

##alien_color = 'green'
##alien_color = 'yellow'
##alien_color = 'red'

if alien_color == 'green':
    print('5 points')
elif alien_color == 'yellow':
    print('10 points')
else:
    print('15 points')


##5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
##stage of life. Set a value for the variable age, and then:
##• If the person is less than 2 years old, print a message that the person is
##a baby.
##• If the person is at least 2 years old but less than 4, print a message that
##the person is a toddler.
##• If the person is at least 4 years old but less than 13, print a message that
##the person is a kid.
##• If the person is at least 13 years old but less than 20, print a message that
##the person is a teenager.
##• If the person is at least 20 years old but less than 65, print a message that
##the person is an adult.
##• If the person is age 65 or older, print a message that the person is an
##elder.

age = 12

if age < 2:
    print("baby")

elif age < 4:
    print("toddler")

elif age < 13:
    print("kid")
    
elif age < 20:
    print("teenager")

elif age < 65:
    print("adult")

else:
    print("elder")

##5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
##independent if statements that check for certain fruits in your list.
##• Make a list of your three favorite fruits and call it favorite_fruits.
##• Write five if statements. Each should check whether a certain kind of fruit
##is in your list. If the fruit is in your list, the if block should print a statement,
##such as You really like bananas!


favorite_fruits = ["orange", "peach", "mango"]

if 'orange' in favorite_fruits:
    print(f"You really like oranges.")


##5-8. Hello Admin: Make a list of five or more usernames, including the name
##'admin'. Imagine you are writing code that will print a greeting to each user
##after they log in to a website. Loop through the list, and print a greeting to
##each user:
##• If the username is 'admin', print a special greeting, such as Hello admin,
##would you like to see a status report?
##• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
##logging in again.
##5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
##not empty.
##• If the list is empty, print the message We need to find some users!
##• Remove all of the usernames from your list, and make sure the correct
##message is printed

uname = ['admin', 'Richybenno54', 'Asian_InvAsian', 'Izuchi', 'kuroxshiro']
##uname = []
if uname == []:
    print('We need to find some users!')
else:
    for user in uname:
        if user == 'admin':
            print('Hello, admin, would you like to see a status report?')
        else:
            print(f'Hello, {user}. Thank you for logging in again.')

##5-10. Checking Usernames: Do the following to create a program that simulates
##how websites ensure that everyone has a unique username.
##• Make a list of five or more usernames called current_users.
##• Make another list of five usernames called new_users. Make sure one or
##two of the new usernames are also in the current_users list.
##• Loop through the new_users list to see if each new username has already
##been used. If it has, print a message that the person will need to enter a
##new username. If a username has not been used, print a message saying
##that the username is available.
##• Make sure your comparison is case insensitive. If 'John' has been used,
##'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
##current_users containing the lowercase versions of all existing users.)


current_users = ['admin', 'Richybenno54', 'Asian_InvAsian', 'Izuchi', 'kuroxshiro', 'new1', 'NEW2']
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())
print(current_users_lower)

new_users = ['NEW1', 'new2', 'new3', 'new4', 'new5']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user} is already in use. Please choose another username.')
    else:
        print(f'{new_user} is available')
        

##5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
##as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
##• Store the numbers 1 through 9 in a list.
##• Loop through the list.
##• Use an if-elif-else chain inside the loop to print the proper ordinal ending
##for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
##7th 8th 9th", and each result should be on a separate line.
        
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(f"{number}" + "st")

    elif number == 2:
        print(f"{number}" + "nd")

    elif number == 3:
        print(f"{number}" + "rd")

    else:
        print(f"{number}" + "th")
        










