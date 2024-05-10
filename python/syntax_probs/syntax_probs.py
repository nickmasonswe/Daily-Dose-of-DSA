# This is a file to solve problems in Python focusing on syntax optimizations as I learn more.
# My focus is on improving the syntax of the code, making it more "Pythonic", not necessarily accounting for every single edge case and optimization.


# Declare a recursive function 'divisible' that takes in at least two arguments (a number, and an array of numbers).
# It should return true if ALL numbers in the array are equally divisible by the single number argument. 
# If any of the numbers in the array are not equally divisible, return false. 
# Once complete, write some code to test your 'divisible' function.

def divisible(num,arr):
  for el in arr:
    # can not do 'if el % num is not 0:' bc of error having to do with int values
    if el % num != 0:
      return False
  return True

def divisible_recursive(num,arr):
  if len(arr) == 0:
    return True
  if arr[0] % num != 0:
    return False
    # note that (num,arr[1] did not work and caused Py to throw a type error. Need to have the colon to let it know I am slicing.
  return divisible_recursive(num,arr[1:])


# print(divisible(3,[9,18,6])) #True
# print(divisible(3,[10,18,6])) #False

print(divisible_recursive(3,[9,18,6])) #True
print(divisible_recursive(3,[10,18,6])) #False