# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "stop and smell the roses."

# Start your changes on line 13
sentence = "StopAndSmellTheRoses"

def word_separator(sentence):
    new_sentence = sentence[0].lower()
    for char in sentence [1:]:
        if char.isupper():
            new_sentence += ' '
        new_sentence += char.lower()
    return new_sentence
# Example usage

new_sentence = word_separator(sentence)
print(new_sentence)
