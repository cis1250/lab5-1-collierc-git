#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_input():
  while True:
  while True:
    input = input()
    try:
      terms = int(input)
      break
    except ValueError:
      del input
      print("please input an integer")
  if terms > 0:
    return input
    break
  else:
    del input
    print("please input a positive integer")

def calculate(digits):
  print("calculating fibbonacci sequence up to " + digits + " digits")
  value1 = 0
  value2 = 1
  for x in range (0,digits):
    if x == 0:
      print(value1)
    else:
      value3 = value1 + value2
      value1 = value2
      value2 = value3
      print(value2)

print("please enter the amount of terms you want to print")
terms = get_input()
calculate(terms)
