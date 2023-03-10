# Madlib Word Game
sentence = "Just as I arrived at PLACE, I realized I had forgotten OBJ."
# 1. ask the user for a word (get user input)
place = input("Tell me a place: ")
# 2. replace a section of the story with the user's word
newSentence = sentence.replace("PLACE", place)
# 3. repeat until all the blanks have been filled
obj = input("Now give me an object: ")
finalSentence = newSentence.replace("OBJ", obj)
# 4. print out the final string to the user
print(finalSentence)