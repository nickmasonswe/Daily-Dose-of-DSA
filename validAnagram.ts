/* 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false
Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
*/

//Count number of occurences of each letter in both strings. If they are the same, you have an anagram. If the lengths of string s and string t are not the same, the answer is automatically false. 

function isAnagram(s: string, t: string): boolean {  
  //create hashmap for 's'
  const hashmapS = {};
  const hashmapT = {};
  //loop through 's', adding the letter as a key, and the occurence count as the value.
  for(const letter of s){
      hashmapS.hasOwnProperty(letter) ?
      hashmapS[letter] +=1 :
      hashmapS[letter] = 0
  }
  //likewise for 't' with it's own hashmap
  for(const letter of t){
      hashmapT.hasOwnProperty(letter) ?
      hashmapT[letter] +=1 :
      hashmapT[letter] = 0
  }
  //compare the counts in the hashmaps
  for(const letter in hashmapS) {
      //return false on any discrepancy 
      if(hashmapS[letter] !== hashmapT[letter]) return false;
  }
  //otherwise return true once the maps have been checked completely
  return true;
}

//Space and Time Complexity:
//Space: O(s+t)
//Time: O(s+t)

//Another tricky/fun way of solving is to simply sort the letters of both and compare the two strings sortedS === sortedT
