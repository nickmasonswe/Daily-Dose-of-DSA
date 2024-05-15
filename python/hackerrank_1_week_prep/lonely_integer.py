# Given an array of integers, where all elements but one occur twice, find the unique element.
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def lonelyinteger(a):
    # init a set that will ultimately contain our only unique value
    seen = set()
    for integer in a:
        if integer in seen:
            seen.remove(integer)
        else:
            seen.add(integer)
    return seen.pop()

#XOR operator can make O(n) as well