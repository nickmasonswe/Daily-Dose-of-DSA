function lonelyinteger(a) {
  // Write your code here
  //Let's use the XOR bitwise operator. Will check the bits of the integers and ultimately, if the integer is compared to the same integer, the underlying bits will become 0, while only the unique integer will not be canceled out in this way. This will give O(n) run time.
  let result;
  for (let integer of a) {
    result ^= integer;
  }
  return result;
}

/* 
Given an array of integers, where all elements but one occur twice, find the unique element. 
*/
