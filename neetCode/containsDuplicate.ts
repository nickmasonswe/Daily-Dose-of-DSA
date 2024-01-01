/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
*/

function containsDuplicate(nums: number[]): boolean {
  //create map for tracking seen elements 
  const seen = {};
  //loop thru the array, checking each el against the map
  for(let i = 0; i < nums.length; i++) {
      //if there is a match, return true, short circuit
      if(seen[nums[i]]) return true;
  }
      //if we get to the end and there is not a match, return false
  return false;
};

//Time and Space Complexity
//Time: O(n)
//Space: O(n)

//Could have used a set instead of an object