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
//Write a function that takes two inputs, a base and an exponent, and returns the expected value of base ^ exponent. For instance, if our base is 2 and our exponent is 3, then return 8 because 2^3 = 2*2*2 = 8.

function pow(base, exponent, count = 0, result = 1) {
  //base case
  if (base === 0) return 1;
  if (base === 1) return base;
  if (count === exponent) return result;
  //recursive case
  result *= base;
  return pow(base, exponent, ++count, result);
}

// To check if you've completed the challenge, uncomment these console.logs!
console.log(pow(2, 4)); // -> 16
console.log(pow(3, 5)); // -> 243
/* ------------------------ ------------------------ */
//Write a function that takes an array of functions and a number that will be piped through all those functions. The input number passes through the first function, whose output is passed as input to the second function, whose output is passed as input to the third function, and so on. Use recursion to return the final output of the last function in the array.

function flow(input, funcArray) {
  //base case
  if (!funcArray[0]) return input;
  //recursive case
  input = funcArray[0](input);
  return flow(input, funcArray.slice(1));
}

// To check if you've completed the challenge, uncomment this code!
function multiplyBy2(num) {
  return num * 2;
}
function add7(num) {
  return num + 7;
}
function modulo4(num) {
  return num % 4;
}
function subtract10(num) {
  return num - 10;
}
const arrayOfFunctions = [multiplyBy2, add7, modulo4, subtract10];
console.log(flow(2, arrayOfFunctions)); // -> -7
/* ------------------------ ------------------------ */

/* ------------------------ ------------------------ */
