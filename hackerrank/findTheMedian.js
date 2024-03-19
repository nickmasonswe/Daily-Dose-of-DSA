function findMedian(arr) {
  // Write your code here
  const sortedArr = arr.sort((a, b) => a - b);
  let result;
  if (sortedArr.length % 2 === 0) {
    result = sortedArr[sortedArr.length / 2];
  } else result = sortedArr[(sortedArr.length - 1) / 2];
  return result;
}
