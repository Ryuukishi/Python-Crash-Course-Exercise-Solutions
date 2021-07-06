##4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
##pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['Margherita', 'Quattro Formaggi', 'Hawaiian']
for pizza in pizzas:
    print(pizza)

##• Modify your for loop to print a sentence using the name of the pizza
##instead of printing just the name of the pizza. For each pizza you should
##have one line of output containing a simple statement like I like pepperoni
##pizza.

pizzas = ['Margherita', 'Quattro Formaggi', 'Hawaiian']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
    
##• Add a line at the end of your program, outside the for loop, that states
##how much you like pizza. The output should consist of three or more lines
##about the kinds of pizza you like and then an additional sentence, such as
##I really love pizza!

pizzas = ['Margherita', 'Quattro Formaggi', 'Hawaiian']
for pizza in pizzas:
    print(f"I like {pizza} pizza.\n")
print("I really love pizza.")


##4-2. Animals: Think of at least three different animals that have a common characteristic.
##Store the names of these animals in a list, and then use a for loop to
##print out the name of each animal.

animals = ['cats', 'tigers', 'lions']
for animal in animals:
    print(animal)


##• Modify your program to print a statement about each animal, such as
##A dog would make a great pet.

for animal in animals:
    print(f"A {animal} would make a great pet.")
    
##• Add a line at the end of your program stating what these animals have in
##common. You could print a sentence such as Any of these animals would
##make a great pet!

for animal in animals:
    print(f"A {animal} would make a great pet.")
print("All these animals are felines.")


##4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
##inclusive.

for number in range(1,21):
    print(number)

##4-4. One Million: Make a list of the numbers from one to one million, and then
##use a for loop to print the numbers. (If the output is taking too long, stop it by
##pressing ctrl-C or by closing the output window.)

##for number in range(1,1_000_001):
##    print(number)
    
##with open(r"C:/Million.txt","w",encoding='utf8') as outfile:
##    for number in range(1,1_000_001):
##        outfile.write(str(number)+"\n")

##4-5. Summing a Million: Make a list of the numbers from one to one million,
##and then use min() and max() to make sure your list actually starts at one and
##ends at one million. Also, use the sum() function to see how quickly Python can
##add a million numbers.

number = range(1,1000001)

print(min(number))
print(max(number))
print(sum(number))
    
##4-6. Odd Numbers: Use the third argument of the range() function to make a
##list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd = []
for value in range(1,21,2):
    odd.append(value)
print(odd)
    
##4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
##print the numbers in your list.

multiples=[]
for value in range(3,31,3):
    multiples.append(value)
print(multiples)
    
##4-8. Cubes: A number raised to the third power is called a cube. For example,
##the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
##is, the cube of each integer from 1 through 10), and use a for loop to print out
##the value of each cube.
cubes=[]
for value in range(1,11):
    cube=value**3
    cubes.append(cube)
print(cubes)
    
##4-9. Cube Comprehension: Use a list comprehension to generate a list of the
##first 10 cubes.

##cubes = [cube**3 for cube in range(1,11)]
##print(cubes)
##
##numbers=[]
##for number in range(1,11):
##    numbers.append(number)
##print(numbers[0:-2:-1])
##

##4-10. Slices: Using one of the programs you wrote in this chapter, add several
##lines to the end of the program that do the following:
##• Print the message The first three items in the list are:. Then use a slice to
##print the first three items from that program’s list.


print(f"The first three items in the list are:{cubes[0:3]}.")


##• Print the message Three items from the middle of the list are:. Use a slice to
##print three items from the middle of the list.

print(f"Three items from the middle of the list are:{cubes[4:7]}.")

##• Print the message The last three items in the list are:. Use a slice to print the
##last three items in the list.

print(f"The last three items in the list are:{cubes[-3:]}.")

##4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
##(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.

friend_pizzas = pizzas[:]

##Then, do the following:
##• Add a new pizza to the original list.

pizzas.append("Seafood")

##• Add a different pizza to the list friend_pizzas.

friend_pizzas.append("Marinara")

##• Prove that you have two separate lists. Print the message My favorite
##pizzas are:, and then use a for loop to print the first list. Print the message
##My friend’s favorite pizzas are:, and then use a for loop to print the second
##list. Make sure each new pizza is stored in the appropriate list.

print(f"My favourite pizzas are:{pizzas}.")

print(f"My friend's favourite pizzas are:{friend_pizzas}.")

##4-12. More Loops: All versions of foods.py in this section have avoided using
##for loops when printing to save space. Choose a version of foods.py, and
##write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print(f"\nMy favorite foods are:{food}.")

for food in friend_foods:
    print(f"\nMy friend's favorite foods are:{food}.")


##4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
##simple foods, and store them in a tuple.

menu = ("fries", "pizza", "burger", "ice cream", "coke")

##• Use a for loop to print each food the restaurant offers.

for item in menu:
    print(item)

##• Try to modify one of the items, and make sure that Python rejects the
##change.

##menu[0] = "chips"
    
##• The restaurant changes its menu, replacing two of the items with different
##foods. Add a line that rewrites the tuple, and then use a for loop to print
##each of the items on the revised menu.

menu = ("chips", "calzone", "burger", "ice cream", "coke")

for item in menu:
    print(item)

















