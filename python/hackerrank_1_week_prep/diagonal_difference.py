# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def diagonalDifference(arr):
    # Write your code here
    left_sum = 0
    right_sum = 0
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if i == j:
                left_sum+= arr[i][j]
            if i+j == n-1:
                right_sum+= arr[i][j]
    return abs(left_sum - right_sum)