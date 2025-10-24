# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random


#Define your dictionary

#Ask 5 random questions and keep track of score.
#loop on dictionary
#randomly print a province and ask for capital
#check response
#if right add to score
#if wrong add to fail score

#output score.

canada_capitals = {
    "Alberta": "Edmonton",
    "British Columbia": "Victoria",
    "Manitoba": "Winnipeg",
    "New Brunswick": "Fredericton",
    "Newfoundland and Labrador": "St. John's",
    "Nova Scotia": "Halifax",
    "Ontario": "Toronto",
    "Prince Edward Island": "Charlottetown",
    "Quebec": "Quebec City",
    "Saskatchewan": "Regina"
}
correct = 0
incorrect = 0
for quiz in range(0,5):
    province = random.choice(list(canada_capitals.keys()))
    answer = input(f"What is the capital of {province}: ")
    if answer == canada_capitals[province]:
        print(f"Correct! The capital of {province} is {answer}")
        correct += 1
    else:
        print(f"Incorrect! The capital of {province} is {canada_capitals[province]}")
        incorrect += 1

print (f"You have {correct} correct answers.")
print (f"You have {incorrect} incorrect answers.")
