function miniMaxSum(arr) {
  arr.sort((a, b) => a - b);
  const maxArr = arr.slice(1);
  const minArr = arr.slice(0, -1);
  const maxSum = maxArr.reduce(add);
  const minSum = minArr.reduce(add);
  console.log(minSum, maxSum);
}
function add(a, b) {
  return a + b;
}

/* 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5

Sample Output

10 14

Hints: Beware of integer overflow! Use 64-bit Integer.
*/
