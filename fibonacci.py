#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_input():
  while True:
    while True:
      test = input()
      try:
        terms = int(test)
        break
      except ValueError:
        del test
        print("please input an integer")
    if terms > 0:
      break
    else:
      del test
      print("please input a positive integer")
  return terms

def calculate(digits):
  print("calculating fibbonacci sequence up to " + str(digits) + " digits")
  value1 = 0
  value2 = 1
  temp = []
  
  for x in range (0,digits):
    if x == 0:
      temp.append(value1)
    else:
      value3 = value1 + value2
      value1 = value2
      value2 = value3
      temp.append(value1)
  return temp

def print_sequence(list):
  print(list)

print("please enter the amount of terms you want to print")
terms = get_input()
sequence = calculate(terms)
print_sequence(sequence)
