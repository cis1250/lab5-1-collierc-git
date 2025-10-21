#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    #loop to check if its a sentence, is only broken once valid input is recieved
    while True:
        user_sentence = input("Enter a sentence: ")
        if is_sentence(user_sentence): 
            break
        else:
            print("please enter a valid sentence")
    return user_sentence

def calculate_frequencies(user_sentence):
    list1 = user_sentence.split(' ')
    list1[0] = list1[0].lower() #use the first index to remove the capital letter
    list1[-1] = list1[-1][:-1] #using negaite indexing to acces the last element and remove the period
    tempset = set(list1) #turning the sentence into a set to remove repeaded words
    list2 = list(tempset) #making another set with removed repeated words
    list3 = [0]*len(list2) #making a third list to store the repitition of words
    for words in list1:
        list3[list2.index(words)] += 1 #once it sees a word in the sentence adds one to the integer in the counting list
    return list2, list3 #return the list without repitition and the list which counts the frequency

def print_frequencies(list1, list2):
    for words in list1:
        print(words + ":")
        print(list2[list1.index(words)])

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

main()
    

