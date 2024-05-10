# This is a file to solve problems in Python focusing on syntax optimizations as I learn more.
# My focus is on improving the syntax of the code, making it more "Pythonic", not necessarily accounting for every single edge case and optimization.


# Declare a recursive function 'divisible' that takes in at least two arguments (a number, and an array of numbers).
# It should return true if ALL numbers in the array are equally divisible by the single number argument. 
# If any of the numbers in the array are not equally divisible, return false. 
# Once complete, write some code to test your 'divisible' function.

def divisible(num,arr):
  for el in arr:
    if el % num != 0:
      return False
  return True

print(divisible(3,[9,18,6])) #True
print(divisible(3,[10,18,6])) #False
