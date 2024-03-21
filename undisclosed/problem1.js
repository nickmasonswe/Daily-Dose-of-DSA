function arrayUpdate(arr) {
  const arrSum = arr.reduce((a, b) => (a += b));
  const targetMin = arrSum / arr.length;
  let result = Math.floor(targetMin + 1);
  return result;
}

const test1 = [1, 2, 3, 4, 5];
const test2 = [1, 2, 3, 4, 9];
const test3 = [1, 2, 3, 4, 21];
const test4 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

console.log(arrayUpdate(test1));
console.log(arrayUpdate(test2));
console.log(arrayUpdate(test3));
console.log(arrayUpdate(test4));
