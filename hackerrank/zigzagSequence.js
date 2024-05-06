function processData(input) {
  //Enter your code here
  const k = (input.length + 1) / 2;
  const tempIncreasing = [];
  const tempDecreasing = [];
  for (let i = 0; i < k; i++) {
    tempIncreasing.push(input[i]);
  }
  // console.log(tempIncreasing);
  for (let i = k; i < input.length; i++) {
    tempDecreasing.push(input[i]);
  }
  console.log(tempDecreasing);
  const increasingHalf = tempIncreasing.sort((a, b) => b - a);
  // const decreasingHalf = tempDecreasing.sort((a, b) => b - a);
  console.log(increasingHalf);
  // console.log(decreasingHalf);
  const concattedArr = tempDecreasing.concat(increasingHalf);
  // console.log(6%2);
  return concattedArr;
}

const a = [2, 3, 5, 1, 4];
const zigZagSeq = processData(a);
console.log(zigZagSeq); // Output: [1, 4, 5, 3, 2]
