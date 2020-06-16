# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

newhumans = []

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for x in range(10):
    if humans[x].name[0:1] == 'D':
        a.append(humans[x].name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for x in range(10):
    if humans[x].name[-1:] == 'e':
        b.append(humans[x].name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
for x in range(10):
    if humans[x].name[0:1] == 'C' or humans[x].name[0:1] == 'D' or humans[x].name[0:1] == 'E' or humans[x].name[0:1] == 'F' or humans[x].name[0:1] == 'G':
        c.append(humans[x].name) 
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
for x in range(10):
    newage = humans[x].age + 10
    d.append(newage)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for x in range(10):
    e.append(humans[x].name + '-'+ str(humans[x].age))
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for x in range(10):
    if humans[x].age >= 27 and humans[x].age <=32:
        empty_tuple = (humans[x].name, humans[x].age)
        f.append(empty_tuple)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for x in range(10):
    #  newhumans[x] = humans[x]
    #  newhumans[x].name = humans[x].name.upper
    human_instance = Human(humans[x].name.upper(), humans[x].age)
    g.append(human_instance)
    #  g.append(newhuman[x])
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
for x in range(10):
    h.append(math.sqrt(humans[x].age))
print(h)
