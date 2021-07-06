##3-1. Names: Store the names of a few of your friends in a list called names. Print
##each person’s name by accessing each element in the list, one at a time.

friends = ['Div', 'Jason', 'Billy', 'Clark', 'Shamil', 'Carlos']
friends = ['Carlos', 'Billy', 'Jason', 'Div', 'Clark', 'Shamil']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
print("\n")
print(*friends, sep="\n")       #print each item in list one by one in new line
print("\n")
for i in range(len(friends[::-1])):   #alternative method
    print(friends[i].upper())
print("\n")
print(*friends[::-1], sep="\n") #print names in reverse
print("\n")
x = ["one", "two", "three"] ; print(x)
x = x[::-1]; x = [element.upper() for element in x] ; print(x)
x = x[::-1]; x = [element.lower() for element in x] ; print(x)

mylist = ['asasdd', 'abc', 'cda']
for item in reversed(mylist):
    print(f"{item.upper()}")

print(f"My most recent friend is {friends[-1]}.")

##3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
##printing each person’s name, print a message to them. The text of each message
##should be the same, but each message should be personalized with the
##person’s name.
for i in range(len(friends)):
    print(f"Hello, {friends[i]}.")
    
##3-3. Your Own List: Think of your favorite mode of transportation, such as a
##motorcycle or a car, and make a list that stores several examples. Use your list
##to print a series of statements about these items, such as “I would like to own a
##Honda motorcycle.”


motorcycles = ['honda', 'yamaha', 'suzuki']
for i in range(len(motorcycles)):
    print(f"I want to own a {motorcycles[i].title()} motorcycle.")

##3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
##would you invite? Make a list that includes at least three people you’d like to
##invite to dinner. Then use your list to print a message to each person, inviting
##them to dinner.

guests = ['Carlos', 'Billy', 'Jason', 'Div', 'Clark', 'Shamil']
for i in range(len(guests)):
    print(f"Hey, {guests[i]}. Want to come to my party?\n")
    
##3-5. Changing Guest List: You just heard that one of your guests can’t make the
##dinner, so you need to send out a new set of invitations. You’ll have to think of
##someone else to invite.
##• Start with your program from Exercise 3-4. Add a print() call at the end
##of your program stating the name of the guest who can’t make it.
##• Modify your list, replacing the name of the guest who can’t make it with
##the name of the new person you are inviting.
##• Print a second set of invitation messages, one for each person who is still
##in your list.

print(f"{guests[0]} can't make it.\n")
guests[0] = 'Shella'
for i in range(len(guests)):
    print(f"Hey, {guests[i]}. Want to come to my party?\n")


##3-6. More Guests: You just found a bigger dinner table, so now more space is
##available. Think of three more guests to invite to dinner.
##• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
##call to the end of your program informing people that you found a bigger
##dinner table.
##• Use insert() to add one new guest to the beginning of your list.
##• Use insert() to add one new guest to the middle of your list.
##• Use append() to add one new guest to the end of your list.
##• Print a new set of invitation messages, one for each person in your list.

for i in range(len(guests)):
    print(f"Hey, {guests[i]}. I just found a bigger dinner table.\n")

guests.insert(0, 'Rowie')
print(guests)
guests.insert(len(guests)//2, 'Robert')
print(guests)
guests.append('Charlene')
for i in range(len(guests)):
    print(f"Hey, {guests[i]}. Want to come to my party?\n")

##3-7. Shrinking Guest List: You just found out that your new dinner table won’t
##arrive in time for the dinner, and you have space for only two guests.
##• Start with your program from Exercise 3-6. Add a new line that prints a
##message saying that you can invite only two people for dinner.

for i in range(len(guests)):
    print(f"Hey, {guests[i]}. Sorry, but we can only invite two people for dinner.\n")
    
##• Use pop() to remove guests from your list one at a time until only two
##names remain in your list. Each time you pop a name from your list, print
##a message to that person letting them know you’re sorry you can’t invite
##them to dinner.

while len(guests) > 2:
    removed = guests.pop(0)
    print(f"Sorry, {removed}")
    print(guests)
    
##• Print a message to each of the two people still on your list, letting them
##know they’re still invited.

for i in range(len(guests)):
    print(f"Hey, {guests[i]}. You're still invited to dinner.\n")
    
##• Use del to remove the last two names from your list, so you have an empty
##list. Print your list to make sure you actually have an empty list at the end
##of your program.

del guests[0:2]
print(guests)


