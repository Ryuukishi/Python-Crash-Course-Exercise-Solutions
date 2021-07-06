##6-1. Person: Use a dictionary to store information about a person you know.
##Store their first name, last name, age, and the city in which they live. You
##should have keys such as first_name, last_name, age, and city. Print each
##piece of information stored in your dictionary.

personal_details = {'first_name': 'Richard', 'last_name': 'Cho', 'age': '26', 'city': 'Shiroishi'}

print(personal_details['first_name'])
print(personal_details['last_name'])
print(personal_details['age'])
print(personal_details['city'])

##6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
##Think of five names, and use them as keys in your dictionary. Think of a favorite
##number for each person, and store each as a value in your dictionary. Print
##each person’s name and their favorite number. For even more fun, poll a few
##friends and get some actual data for your program.

fav_nums = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}
for name, fav_num in fav_nums.items():
    print(f"Name: {name}")
    print(f"Favorite Number: {fav_num}")

##6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
##up the code from Exercise 6-3 (page 99) by replacing your series of print()
##calls with a loop that runs through the dictionary’s keys and values. When
##you’re sure that your loop works, add five more Python terms to your glossary.
##When you run your program again, these new words and meanings should
##automatically be included in the output.

fav_nums['f'] = '6'
fav_nums['g'] = '7'
fav_nums['h'] = '8'
for name, fav_num in fav_nums.items():
    print(f"Name: {name}")
    print(f"Favorite Number: {fav_num}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
'nile': 'egypt',
'amazon': 'brazil',
'ganges' : 'india'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through the {country.title()}.")

for river in rivers.keys():
    print(f"{river.title()}")

for country in rivers.values():
    print(f"{country.title()}")

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

people = ['jen', 'sarah', 'edward', 'phil', 'richard', 'shamil']
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for person in people:
    if person in favorite_languages:
        print(f"{person.title()} has already completed a poll.")
    else:
        print(f"{person.title()} has not completed a poll.")


##6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
##Make two new dictionaries representing different people, and store all three
##dictionaries in a list called people. Loop through your list of people. As you
##loop through the list, print everything you know about each person.

richard_1 = {'first_name': 'Richard', 'last_name': 'Cho', 'age': '26', 'city': 'Shiroishi'}
richard_2 = {'first_name': 'Shamil', 'last_name': 'Auwal', 'age': '21', 'city': 'Shichikashuku'}
richard_3 = {'first_name': 'Shella', 'last_name': 'Wu', 'age': '25', 'city': 'Sendai'}

richards = [richard_1, richard_2, richard_3]

for richard in richards:
    print(f"My name is {richard['first_name']} {richard['last_name']}. I am {richard['age']} and I live in {richard['city']}.")

##6-8. Pets: Make several dictionaries, where each dictionary represents a different
##pet. In each dictionary, include the kind of animal and the owner’s name.
##Store these dictionaries in a list called pets. Next, loop through your list and as
##you do, print everything you know about each pet.

shiba= {'type': 'dog', 'owner': 'shella'}
simba = {'type': 'lion', 'owner': 'jason'}
nyanko = {'type': 'cat', 'owner': 'richard'}

pets= [shiba, simba, nyanko]

for pet in pets:
    print(f"Type: {pet['type']}. Owner: {pet['owner'].title()}")

##6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
##names to use as keys in the dictionary, and store one to three favorite places
##for each person. To make this exercise a bit more interesting, ask some friends
##to name a few of their favorite places. Loop through the dictionary, and print
##each person’s name and their favorite places.

favorite_places = {'Richard': 'Hokkaido', 'Div': 'Fukushima', 'Shella': 'Nagoya'}
for person, place in favorite_places.items():
    print(f"{person.title()}'s favorite place in Japan is {place.title()}.")




