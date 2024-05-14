# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to are acceptable.

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# This worked, but using template literal was not my first choice. 
# I originally got type error from trying to use a regular string and '+' the floats to the strings.
# An alternative route that looks good is using the .format() method which I have seen a few times now:

# print("{:.6f}\n{:.6f}\n{:.6f}".format(positive, negative, zero))
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive+=1
        elif num < 0:
            negative +=1
        else:
            zero+=1
    positive_ratio = float(positive_ratio/len(arr))
    negative_ratio = float(negative/len(arr))
    zero_ratio = float(zero/len(arr))
    print(f'{positive_ratio} \n {negative_ratio} \n {zero_ratio}')
    #see line 15