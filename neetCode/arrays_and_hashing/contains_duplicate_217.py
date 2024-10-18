from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #counter hashmap, if any are greater than 1 return true else retun false
        count_map = Counter()
        for num in nums:
            if num in count_map:
                return True
            count_map[num] += 1
        return False

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))