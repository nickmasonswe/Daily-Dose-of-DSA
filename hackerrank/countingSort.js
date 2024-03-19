function countingSort(arr) {
  //create a frequency array
  const result = new Array(100).fill(0);
  for (const el of arr) {
    result[el]++;
  }
  return result;
}
/* 
Note
For this exercise, always return a frequency array with 100 elements. The example above shows only the first 4 elements, the remainder being zeros.

Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.
*/
