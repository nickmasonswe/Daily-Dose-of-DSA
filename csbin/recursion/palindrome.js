/* Palindrome
Create a recursive function palindrome that accepts a string as an input and returns true if that
string is a palindrome (the string is the same forward and backwards). The input string may have
punctuation and symbols, but that should not affect whether the string is a palindrome.
*/
//case insensitive
//look at the first and last letter.

const palindrome = string => {
  let upperCasedString = string.toUpperCase().replace(/\W/g, '');
  if (string.length < 2) return true;
  if (upperCasedString[0] !== upperCasedString.at(-1)) return false;
  return palindrome(upperCasedString.slice(1, -1));
};

console.log(palindrome('Anne, I vote more cars race Rome-to-Vienna')); //-> true
console.log(palindrome('llama mall')); //-> true
console.log(palindrome('jmoney')); //-> false
