/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*/

//Unoptimized v.1
function topKFrequent(nums, k) {
  //init a hashmap to track the elements and their frequencies
  const hashmap = {};
  //declare a return array that will house the value of the elements at the given ith index later
  const result = [];
  //loop through the nums array, and place the elements into the hashmap appropriately
  for (let i = 0; i < nums.length; i++) {
    hashmap[nums[i]] ? (hashmap[nums[i]] += 1) : (hashmap[nums[i]] = 1);
  }
  //use object.keys to make an array of the keys that are in the hashmap
  const keys = Object.keys(hashmap);
  //sort the keys in descending order and save to a variable (sort converts to a string by default)
  const sortedKeys = keys.sort((a, b) => hashmap[b] - hashmap[a]);
  //loop through the values k amount of times, pushing the current value each time
  for (let i = 0; i < k; i++) {
    //add the Number version of the value to the return array (bc sort converts to string) which should be k length if the element is not the first.
    result.push(Number(sortedKeys[i]));
  }
  return result;
}

//Time: O(n log n + k) because of sorting algo + loop up to k
//Space: O(n +k)
