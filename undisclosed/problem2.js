function processData(input) {
  // loop 1/2 array.length + 1) /2
  // sort
  // loop thru remaining and sort. concat to former
  const k = (input.length + 1) / 2;
  const tempIncreasing = [];
  const tempDecreasing = [];
  for (let i = 0; i < k; i++) {
    tempIncreasing.push(input[i]);
  }
  for (let i = k + 1; i < input.length; i++) {
    tempDecreasing.push(input[i]);
  }
  const increasingHalf = tempIncreasing.sort((a, b) => a - b);
  const decreasingHalf = tempDecreasing.sort((a, b) => b - a);
  const concattedArr = increasingHalf.concat(decreasingHalf);
  const stringVer = concattedArr.join(' ');
  console.log(stringVer);
}
