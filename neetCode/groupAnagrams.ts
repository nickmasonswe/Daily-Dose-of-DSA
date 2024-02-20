/*
49. Group Anagrams
Medium
Topics
Companies

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

*/

function groupAnagrams(strs: string[]): string[][] {
    //init an hashtable where key->sorted letters, val->each word that contains these letters
    const hash = {};
    //loop through the array and sort the letters in each word 
    for(const word of strs) {
        const sorted = word.split("").sort().join("");
    //check if the hash already has a key that matches the sorted version of the current word
        //if so, push the unsorted word to the array associated with the sorted key
        if(hash[sorted]) {
            hash[sorted].push(word);
            //if not, assign an array containing that unsorted word to the associated sorted key
        } else {
            hash[sorted] = [word];
        }
    }
    //return an array containing all of the values from the hash
    return Object.values(hash);
};

//Settled on the sorting method of solving this problem. 
//Time: O(m * n logn) (m being the length of the array)
//Space: O(m * n)