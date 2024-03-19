function diagonalDifference(arr) {
  let diagonal1 = 0;
  let diagonal2 = 0;
  //2D matrix. loop through and find the elements where i and j loop meet for diagonal1. Find the elements where the sum of i and j matches n-1. These indices are always the one you are looking for. i.e [0][2],[1,2], [2,1], [3,0] all sum up to three and would be the desired indices.
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (i === j) diagonal1 += arr[i][j];
      if (i + j === arr.length - 1) diagonal2 += arr[i][j];
    }
  }
  return Math.abs(diagonal1 - diagonal2);
}

/* 
Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
*/
