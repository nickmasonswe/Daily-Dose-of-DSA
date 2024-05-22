class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for el in nums:
            if el in hashset:
                return True
            else:
                hashset.add(el)
        return False

#use set bc if use a normal arr, run time is O(n^2), while lookup on set is O(1) making runtime O(n) wultimately
#remember set is lower cased, and sets .add, while lists .append (not push like js)