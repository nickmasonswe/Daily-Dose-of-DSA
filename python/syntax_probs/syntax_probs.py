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
  def do_math(operator, number):
    if not number:
      return initialValue
    else:
      if operator == '+':
        initialValue += number
      elif operator == '-':
        initialValue -= number
      elif operator == '*':
        initialValue *= number
      elif operator == '/':
        initialValue /= number
      elif operator == '//':
        initialValue //= number
      

      return "Press enter '=' to see the result!"
  return do_math

calculate_4 = calculate(4)
calculate_4('*',2)
print(calculate_4('='))
  

#Get the length of an array using recursion without accessing its length property.

def recursive_length(arr, length=0):
  if not arr[0]:
    return length
  # 'if not arr[0]: did not work because left out empty array on end. not arr is what I was looking for 
  return recursive_length(arr[1:],length+1)

print(recursive_length([1,2,3,4,5,'6',[]])) #7