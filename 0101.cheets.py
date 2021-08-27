#%%
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))
# %%
fav_numbers = {'eric': 17, 'ever': 4}
for name in fav_numbers.keys():
 print(name + ' loves a number')
# %%
fav_numbers = {'eric': 17, 'ever': 4}
for number in fav_numbers.values():
 print(str(number) + ' is a favorite')
# %%
current_value = 1
while current_value <= 5:
 print(current_value)
 current_value += 1
# %%
def make_pizza(topping='bacon'):
 """Make a single-topping pizza."""
 print("Have a " + topping + " pizza!")
make_pizza()
make_pizza('pepperoni')

# %%
class Dog():
    def __init__(self, name):
        self.name = name
    
    def sit(self):
        print(self.name + " is sitting.")

#%%    
my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()

# %%
class SARDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    def search(self):
        print(self.name + " is searching.")

#%%
my_dog = SARDog('Willie')
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()

# %%
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']

# %%
first_three = finishers[:3]

# %%
first_three
# %%
middle_three = finishers[1:4]
# %%
middle_three

# %%
names = ['kai', 'abe', 'ada', 'gus', 'zoe']
# %%
upper_names = [name.upper() for name in names]
# %%
upper_names

# %%
dimensions = (800, 600)
#%%
print(dimensions)
#%%
dimensions = (1200, 900)

# %%
dogs = []

#%%
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')
#%%
dogs
#%%
for dog in dogs:
    print("Hello " + dog + "!")
#%%
print("I love these dogs!")
print("\nThese were my first two dogs:")

#%%
old_dogs = dogs[:2]

for old_dog in old_dogs:
    print(old_dog)
#%%
del dogs[0]
#%%
dogs.remove('peso')
#%%
print(dogs)

# %%
alien_0 = {'color': 'green', 'points': 5}

#%%
print(alien_0['color'])
print(alien_0['points'])

# %%
alien_0 = {'color': 'green'}

#%%
alien_color = alien_0.get('color')

#%%
alien_color
#%%
alien_points = alien_0.get('points', 0)
alien_points
#%%
print(alien_color)
print(alien_points)

# %%
alien_0['x'] = 0
alien_0['y'] = 25
alien_0['speed'] = 1.5
# %%
alien_0

# %%
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

# %%
alien_0

# %%
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)

#%%
user = []


# %%
new_user = {
'last': 'fermi',
'first': 'enrico',
'username': 'efermi',
}
#%%
user.append(new_user)
# %%
new_user = {
'last': 'curie',
'first': 'marie',
'username': 'mcurie',
}
user.append(new_user)
user# %%

# %%
for user_dict in user:
    for k, v in user_dict.items():
        print(k + ": " + v)
        print("\n")

# %%
fav_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

#%%
for name, langs in fav_languages.items():
    print(name + ": ")
    for lang in langs:
        print("- " + lang)


# %%
for name in fav_languages.values():
    print(name)

# %%
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
# %%
for usermame, u_dict in users.items():
     print("\n Username"+ usermame)
     fullname = user_dict['first'] + " "
     fullname += user_dict['last']
     l = user_dict['location']

     print("Full Name"+ fullname.title())
     print("Location"+ l.title())
# %%
for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
# %%
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your cost is $" + str(price) + ".")
# %%

players = []
#%%
if players:
    for player in players:
        print("Player: " + player.title())
    else:
        print("We have no players yet!")
# %%
banned_users = ['eve', 'fred', 'gary', 'helen']
prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "
#%%
players = []

#%%
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)

#%%    
print("\nYour team:")
for player in players:
    print(player)

# %%
pets = ['dog', 'cat', 'dog', 'fish', 'cat','rabbit', 'cat']
print(pets)

#%%
while 'cat' in pets:
    pets.remove('cat')

#%%
print(pets)

# %%
def describe_pet(animal, name=None):
    print("\nI have a " + animal + ".")
    if name:
        print("Its name is " + name + ".")
#%%
describe_pet('hamster', 'harry')
describe_pet('snake')
# %%
def build_person(first, last):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last': last}
    return person
# %%
musician = build_person('jimi', 'hendrix')
print(musician)

# %%
def build_person(first, last, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person
# %%
musician = build_person('jimi', 'hendrix', 27)
print(musician)
#%%
musician = build_person('janis', 'joplin')
print(musician)

# %%
def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)

#%%
# Store some unprinted designs,
# and print each of them.
unprinted = ['phone case', 'pendant', 'ring']
printed = []
#%%
print_models(unprinted, printed)
print("\nUnprinted:", unprinted)
print("Printed:", printed)

# %%
def print_models(unprinted, printed):
    """3d print a set of models."""
    while unprinted:
        current_model = unprinted.pop()
        print("Printing " + current_model)
        printed.append(current_model)

#%%        
# Store some unprinted designs,
# and print each of them.
original = ['phone case', 'pendant', 'ring']
printed = []
#%%
print_models(original[:], printed)
print("\nOriginal:", original)
print("Printed:", printed)

# %%
def make_pizza(size, *toppings):
    """Make a pizza."""
    print("\nMaking a " + size + " pizza.")
    print("Toppings:")
    for topping in toppings:
        print("- " + topping)

#%%        
make_pizza('small', 'pepperoni')
make_pizza('large', 'bacon bits', 'pineapple')
make_pizza('medium', 'mushrooms', 'peppers','onions', 'extra cheese')

# %%
def adding_what_you_need(qunatity=None, *add_on):
    """Making Shake of your wish"""
    print("\n Qunatity of "+qunatity + " Shake")
    print("Add ons:")
    for addon in add_on:
        print("-" + addon)

#%%
adding_what_you_need("300ml","kitkat","chocochips")
# %%
adding_what_you_need("200ml","kitkat","chocochips")


# %%
def build_profile(first, last, **user_info):
    """Build a user's profile dictionary."""
    # Build a dict with the required keys.
    profile = {'first': first, 'last': last}
    # Add any other keys and values.
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

# %%
user_0 = build_profile('albert', 'einstein',location='princeton')
user_1 = build_profile('marie', 'curie',location='paris', field='chemistry')
# %%
print(user_0)
print(user_1)


# %%
import pizza

pizza.make_pizza("small","tomata")


# %%
class Car():
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self.make = make
        self.model = model
        self.year = year
        
        # Fuel capacity and level in gallons.
        
        self.fuel_capacity = 15
        self.fuel_level = 0
    
    def fill_tank(self):
        """Fill gas tank to capacity."""
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")
    
    def drive(self):
        """Simulate driving."""
        print("The car is moving.")


# %%
my_car = Car('audi', 'a4', 2016)
# %%
print(my_car.make)
print(my_car.model)
print(my_car.year)
# %%
my_car.fill_tank()
my_car.drive()
# %%
my_car = Car('audi', 'a4', 2016)
my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('toyota', 'tacoma', 2010)
# %%
my_new_car = Car('audi', 'a4', 2016)
my_new_car.fuel_level = 5
# %%
print(my_new_car)
# %%
filename = "something.txt"

# %%
with open(filename) as f:
    content = f.read()

# %%
print(content)
# %%
with open(filename) as ff:
    for line in ff:
        print(line.rstrip())
# %%
fn = "programming.txt"
# %%
with open(fn,'w') as filee:
    filee.write("I love programming")

# %%
with open(fn,'w') as filee:
    filee.write("I love programming")
    filee.write("\nDon't trust your shadow")

# %%
with open(fn,'a') as filee:
    filee.write("\nFocus")
    filee.write("\nBye")
# %%
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
# %%
f_name = 'siddhartha.txt'

#%%
try:
    with open(f_name) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    msg = "Can't find file {0}.".format(f_name)
    print(msg)
# %%
