print('Hello, world!')

pizza = {
    'size': 'large',
    'toppings': [
        'feta',
        'prosciutto',
        'olives',
        'arugula'
    ],
    'crust': 'gluten free',
    'address': '401 Somewhere St.',
    'note': 'Deliver to treehouse in back yard.'
}

print(pizza)

# name is the variable. it contains a string
name = 'Thomas'
print("Hello, " + name + ", it's nice to meet you.")
# input() is a function that we can pass a parameter in it, becoming a prompt
name = input("Please type your name and press Enter -> ")
print("Hello, " + name + ", it's nice to meet you.")

# variables that contain numbers
taxRate = 0.14
subtotal = 20
tax = subtotal * taxRate
total = subtotal + tax
print('Your total bill is:')
print(total)

# travelDestinations is a variable containing a list
# city is a variable-- its value changes a few times
travelDestinations = ["Almaty", "Moscow", "Buenos Aires", "Manila"]
for city in travelDestinations:
  print(city + " seems like a cool place to go.")

# escape characters - backslash
print("She asked, \"Can't we just leave?\" If only it were that simple.")

# multi-line strings using triple quotes """
prettyValidString = """Hey Jude
Don't make it bad
Take a sad song
And make it better"""

print(prettyValidString)

# concatenation
savory = "peanut butter"
sweet = "jelly"
sandwich = savory + " and " + sweet
print(sandwich)

# strings can have built-in whitespace, ie. \n
# concatenation can happen inside of the print statement
step1 = "Eat\n"
step2 = "Sleep\n"
step3 = "Code\n"
step4 = "Repeat\n"
print(step1+step2+step3+step4)

# substrings
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[0], alphabet[2]) # a c
print(alphabet[-1], alphabet[-4]) # z w

# substring selection --> SLICING
print(alphabet[11:16]) # lmnop, index 11-15
print(alphabet[:5]) # abcde, chars before index 5
print(alphabet[20:]) # uvwxyz, index 20 and onwards

# substring replacement
fullName = "Stanislav Petrov"
differentname = fullName.replace("Stan", "Bob")
print(differentname)

# exercise - string replacement
journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""
correctedJourney = journey.replace("tone", "town")
# "whirl", "world", "tray", "train", "seedy", "city", "Bored", "Born")
print(correctedJourney)

# A number is a mathematical object, used to count, measure, and also label.
# python does not have a data type called "Number"
# integers are whole numbers
# floats are numbers with a decimal
float(2)
print(float)
print(float(2))
int(2.5)
print(int)
print(int(2.5))

# math in python
a = 14
b = 5

# addition
print(a + b)

# multiplication
print(a * b)

# division
print(a / b)

# integer division - round down so there are no decimal places
print(a // b)

# exponentiation (a to the power of b)
print(a ** b)

# compound calculations
c = 8
print(a + b * c ** a)

# compare numbers
# equals
a == b

# doesn't equal
a != b

# greater than
a > b

# greater than or equal to
a >= b

# less than
a < b

# less than or equal to
a <= b

# exercise - tax calculator
# 1. Ask the user to input a subtotal
subtotal = input("Please enter a subtotal -> ")
# 2. Calculate the tax owed using hard-coded tax rate
# convert the string to a number
tax = float(subtotal) * 0.25
# 3. Print out a msg with the amount of tax owed
print(tax)
# 4. Print out another msg with the total owed including tax
print(float(subtotal) + tax)

# exercise - bill splitter
# 1. Ask for a total dollar amount
bill = input("Bill total: ")
# 2. Ask for the percentage tip
tipRate = input("Tip percentage: ")
# 3. Ask for the number of people splitting thebill
people = input("Number of people: ")
# 4. Calculate the amnt each person owes, along with the overall total
tip = float(bill) * float(tipRate)/100
total = float(bill) + float(tip)
print("Overall total: $", str(total))
dividedTotal = float(total) / int(people)
print("Each person should pay: $", dividedTotal)