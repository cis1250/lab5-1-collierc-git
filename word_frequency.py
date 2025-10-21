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
    while True:
        user_sentence = input("Enter a sentence: ")
        if is_sentence(user_sentence):
            break
    return user_sentence

def calculate_frequencies(user_sentence):
    list1 = user_sentence.split(' ')
    tempset = set(list1)
    list2 = list(tempset)
    list3 = [0]*len(list2)
    for words in list1:
        list3[list2.index(words)] += 1
    return list2, list3

def print_frequencies(list1, list2):
    for words in list1:
        print(list1[words] + ":")
        print(list2[list1.index(words)])

def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)

main()
    

