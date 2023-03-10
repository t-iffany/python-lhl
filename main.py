# print('Hello, world!')

# pizza = {
#     'size': 'large',
#     'toppings': [
#         'feta',
#         'prosciutto',
#         'olives',
#         'arugula'
#     ],
#     'crust': 'gluten free',
#     'address': '401 Somewhere St.',
#     'note': 'Deliver to treehouse in back yard.'
# }

# print(pizza)

# # name is the variable. it contains a string
# name = 'Thomas'
# print("Hello, " + name + ", it's nice to meet you.")
# # input() is a function that we can pass a parameter in it, becoming a prompt
# name = input("Please type your name and press Enter -> ")
# print("Hello, " + name + ", it's nice to meet you.")

# # variables that contain numbers
# taxRate = 0.14
# subtotal = 20
# tax = subtotal * taxRate
# total = subtotal + tax
# print('Your total bill is:')
# print(total)

# # travelDestinations is a variable containing a list
# # city is a variable-- its value changes a few times
# travelDestinations = ["Almaty", "Moscow", "Buenos Aires", "Manila"]
# for city in travelDestinations:
#   print(city + " seems like a cool place to go.")

# # escape characters - backslash
# print("She asked, \"Can't we just leave?\" If only it were that simple.")

# # multi-line strings using triple quotes """
# prettyValidString = """Hey Jude
# Don't make it bad
# Take a sad song
# And make it better"""

# print(prettyValidString)

# # concatenation
# savory = "peanut butter"
# sweet = "jelly"
# sandwich = savory + " and " + sweet
# print(sandwich)

# # strings can have built-in whitespace, ie. \n
# # concatenation can happen inside of the print statement
# step1 = "Eat\n"
# step2 = "Sleep\n"
# step3 = "Code\n"
# step4 = "Repeat\n"
# print(step1+step2+step3+step4)

# # substrings
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print(alphabet[0], alphabet[2]) # a c
# print(alphabet[-1], alphabet[-4]) # z w

# # substring selection --> SLICING
# print(alphabet[11:16]) # lmnop, index 11-15
# print(alphabet[:5]) # abcde, chars before index 5
# print(alphabet[20:]) # uvwxyz, index 20 and onwards

# # substring replacement
# fullName = "Stanislav Petrov"
# differentname = fullName.replace("Stan", "Bob")
# print(differentname)

# # exercise - string replacement
# journey = """Just a small tone girl
# Leaving in a lonely whirl
# She took the midnight tray going anywhere
# Just a seedy boy
# Bored and raised in South Detroit or something
# He took the midnight tray going anywhere"""
# correctedJourney = journey.replace("tone", "town")
# # "whirl", "world", "tray", "train", "seedy", "city", "Bored", "Born")
# print(correctedJourney)

# # A number is a mathematical object, used to count, measure, and also label.
# # python does not have a data type called "Number"
# # integers are whole numbers
# # floats are numbers with a decimal
# float(2)
# print(float)
# print(float(2))
# int(2.5)
# print(int)
# print(int(2.5))

# # math in python
# a = 14
# b = 5

# # addition
# print(a + b)

# # multiplication
# print(a * b)

# # division
# print(a / b)

# # integer division - round down so there are no decimal places
# print(a // b)

# # exponentiation (a to the power of b)
# print(a ** b)

# # compound calculations
# c = 8
# print(a + b * c ** a)

# # compare numbers
# # equals
# a == b

# # doesn't equal
# a != b

# # greater than
# a > b

# # greater than or equal to
# a >= b

# # less than
# a < b

# # less than or equal to
# a <= b

# # exercise - tax calculator
# # 1. Ask the user to input a subtotal
# subtotal = input("Please enter a subtotal -> ")
# # 2. Calculate the tax owed using hard-coded tax rate
# # convert the string to a number
# tax = float(subtotal) * 0.25
# # 3. Print out a msg with the amount of tax owed
# print(tax)
# # 4. Print out another msg with the total owed including tax
# print(float(subtotal) + tax)

# # exercise - bill splitter
# # 1. Ask for a total dollar amount
# bill = input("Bill total: ")
# # 2. Ask for the percentage tip
# tipRate = input("Tip percentage: ")
# # 3. Ask for the number of people splitting thebill
# people = input("Number of people: ")
# # 4. Calculate the amnt each person owes, along with the overall total
# tip = float(bill) * float(tipRate)/100
# total = float(bill) + float(tip)
# print("Overall total: $", str(total))
# dividedTotal = float(total) / int(people)
# print("Each person should pay: $", dividedTotal)

# # lists
# emptyList = []

# people = [
#   "Bob",
#   "Jane",
#   "Tim",
#   "Laur",
#   "Udon",
#   "Tiff"
# ]

# # single item
# print(people[3]) # Lau
# print(people[-1]) # Tiff
# print(people[0]) # Bob 

# index = 0
# print(people[index]) # Bob

# # find the index that represents the position in the list
# print(people.index("Tim"))

# # negative list indices
# secondLastPerson = people[-2] # Udon
# print(secondLastPerson)

# # list slicing

# # if we omit the first index = this slice starts at the beginning of the list
# print(people[:3]) # Bob, Jane, Tim
# print(people[2:5]) # Tim, Laur, Udon
# # if we omit the second index = this slice ends at the end of the list
# print(people[4:]) # Udon, Tiff
# print(people[-3:]) # Laur, Udon, Tiff

# # append method - add to end of the list
# people.append("Sarah")
# print(people)

# # insert method - parameter is the index at which we want to insert
# people.insert(2, "Carly")
# print(people)

# # change the value of a list item
# people[2] = "Carly-Rae"
# print(people)

# # del keyword, followed by the item we want to delete
# del people[4]
# print(people)

# # concatenate two lists
# newPeople = [
#   "Yoyo",
#   "Amy"
# ]

# people = people + newPeople
# print(people)

# # exercise - foosball players

# foosballers = [
#   "Mia",
#   "Retta",
#   "Augustine",
#   "Jin",
#   "Waylon",
#   "Alphonso",
#   "Sage",
#   "Hubert",
#   "Raymon",
#   "Rebecca",
#   "Monty",
#   "Glen",
#   "Christi",
#   "Patrice",
#   "Craig",
#   "Dexter",
#   "Wally",
#   "Ian",
#   "Pat"
# ]

# # 1. median player - player exactly in the middle 
# # total # player: len(foosballers) then divide by 2
# index = len(foosballers) / 2
# medianPlayer = foosballers[int(index)]
# print(medianPlayer)

# # 2. five players in the middle - median player + players 2 above and 2 below
# print(foosballers[7:10] + foosballers[10:12])

# # 3. add fake player to the exact middle of the list 
# foosballers.insert(int(len(foosballers)/2), "Average Player")
# print(foosballers)

# # 4. find "Average Player" and change name to uppercase
# foosballers[9] = "AVERAGE PLAYER"
# print(foosballers)

# # 5. add 5 more players with names of your choosing at the bottom of the list
# newPlayers = ["Arlo", "Barb", "Carl", "Dan", "Elle"]
# print(foosballers + newPlayers)

# # 6. fix AVERAGE PLAYER back to middle
# # delete old AVERAGE PLAYER
# del foosballers[9]
# # create new list by adding foosballers and newPlayers
# newList = foosballers + newPlayers
# # find new median player index
# avgPlayerInd = int(len(newList)/2)
# # insert AVERAGE PLAYER to avgPlayerIndex
# newList.insert(avgPlayerInd, "AVERAGE PLAYER")
# print(newList)

# # 7. Five more players show up, but they are ranked. 
# # Insert them at the appropriate location   ????
# hubertInd = newList.index("Hubert")
# newList.insert(hubertInd, "Lacy")

# rebeccaInd = newList.index("Rebecca")
# newList.insert(rebeccaInd, "Omar")
# newList[7] = "Otto"  # newList.insert(7, "Otto")
# newList[-10] = "Chauncey"  # newList.insert(-10, "Chauncey")
# print(newList)

# Looping
# iterate = repeat the same procedure a number of times
clothing = [
  "Shirt",
  "Pants",
  "Socks"
]

# indentation is semantic in python ; indented = part of the code block
for item in clothing:
  foldedItem = "Folded " + item
  print(foldedItem)
print("This line is not part of the `for` loop")

# making new data
instructionSteps = [
  "turn left", 
  "go straight for 2 blocks",
  "turn right",
  "keep going until you see the dog statue",
  "turn right",
  "turn right again",
  "park right on the sidewalk"
]

# start sentence with this ; create instructions variable outside the loop
# so that it wont be overwritten eachtime
instructions = "First, "

# start with instructions, then add nextInstruction and ", then ", and repeat
for nextInstruction in instructionSteps:
  instructions = instructions + nextInstruction + ", then "

print(instructions + "you're there!")

# screamed instructions
instructionStepsButScreamed = []

for nextInstruction in instructionSteps:
  # .upper to convert nextInstruction strings to uppercase
  upperInstruction = nextInstruction.upper()
  # adds a new item to the empty list
  instructionStepsButScreamed.append(upperInstruction)

print(instructionStepsButScreamed)

# iterating over a RANGE
# range: invoke the range function and tell it what #s to start and end at
bacteria = "🥔"

# for each generation between 0 and 10, do:
for generation in range(0, 10):
  # keep doubling the bacteria population for "n" generations
  # where "n" is the difference between first and last # in the range
  bacteria = bacteria + bacteria

print(bacteria)

# import python built-in 'time' library and add pause btwn each generation
import time

bacteria = "🥔"
generations = 10

for generation in range(0, generations):
  bacteria = bacteria * 2
  print(bacteria)
  time.sleep(0.5)