#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers. 

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    min_sum = sum(sorted(sorted_arr[0:-1]))
    max_sum = sum(sorted_arr[1:])
    print('{} {}'.format(min_sum, max_sum))
#Note that I don't need the colon : inside of the braces this time, bc no further formatting needed. See plus_minus.py where needed for floats.