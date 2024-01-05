function twoSum(nums: number[], target: number): number[] {
  // make a hashmap to store elems and their index after visiting them
  const hashmap = {};
  // do one loop through nums array and for each one
  for (let i = 0; i < nums.length; i++) {
      // if this elem is NOT in the hashmap, place it there as key with value being index
      if (!hashmap.hasOwnProperty(nums[i])) {
          hashmap[nums[i]] = i;
      }
      // if an elem exists in the map that strictly equals the difference between the current elem and the target, AND the index/key of hashmap is not the same as the current index, put both indices into an array and return it.
      if (hashmap.hasOwnProperty(target - nums[i]) && hashmap[target - nums[i]] !== i) {
          return [i, hashmap[target - nums[i]]];
      }
  }
}

//Space: O(n)
//Time:  O(n)


/*
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 */

