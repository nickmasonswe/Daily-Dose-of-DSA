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

#print(divisible_recursive(3,[9,18,6])) #True
#print(divisible_recursive(3,[10,18,6])) #False

#Create a functon "buildSentence" that takes any number of words (string) and returns a complete sentence with the first word capitalizated and punctuation (add an exclamation point to each sentence).

def buildSentence(sentence):
  return sentence.title() + '!'

print(buildSentence('hi, You are doing great'))



# Declare a function 'calculate', which takes in a number, initialValue, as a single argument and returns another function.
# The returned function takes up to 2 arguments, a string (it could be any of 4 basic operators: '+', '-', '*', and '/'), a number, or just a single argument. When invoked with two arguments, return the message "Press enter '=' to see the result!". When the returned function is invoked with just an equal sign ('='), return the evaluated result from all previous expressions (starting at the initialValue). 
 # Note: Do not use the 'eval()' method in JS!

def calculate(initialValue):
  def do_math():
    return 0+ initialValue
  
  return do_math

calculate_4 = calculate(4)
print(calculate_4())
  

#Get the length of an array using recursion without accessing its length property.

#/Write a function that takes an array of functions and a number that will be piped through all those functions. The input number passes through the first function, whose output is passed as input to the second function, whose output is passed as input to the third function, and so on. Use recursion to return the final output of the last function in the array.