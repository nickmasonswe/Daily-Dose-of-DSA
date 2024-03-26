//Write a function that takes an input character and returns that character repeated 5 times using recursion. For example, if the input is 'g', then the output should be 'ggggg'.
function repeater(char) {
  //base case
  if (char.length === 5) {
    return char;
  }
  //recursive case
  char += char[0];
  return repeater(char);
}

// To check if you've completed the challenge, uncomment these console.logs!
console.log(repeater('g'));
console.log(repeater('j'));

/* ------------------------ ------------------------ */
//Write a function that returns the factorial of a number.

//EXAMPLE4! = 4 * 3 * 2 * 1 = 24, so calling factorial(4) should return 24.

function factorial(num, result = 1) {
  //base case
  if (num - 1 === 0) return result;
  //recursive case
  result *= num;
  return factorial(num - 1, result);
}

// To check if you've completed the challenge, uncomment these console.logs!
console.log(factorial(4)); // -> 24
console.log(factorial(6)); // -> 720
/* ------------------------ ------------------------ */
//Get the length of an array using recursion without accessing its length property.

function getLength(array, count = 0) {
  //base case
  if (!array[0]) return count;
  //recursive case
  return getLength(array.slice(1), ++count);
}

// To check if you've completed the challenge, uncomment these console.logs!
console.log(getLength([1])); // -> 1
console.log(getLength([1, 2])); // -> 2
console.log(getLength([1, 2, 3, 4, 5])); // -> 5
console.log(getLength([])); // -> 0

/* ------------------------ ------------------------ */
