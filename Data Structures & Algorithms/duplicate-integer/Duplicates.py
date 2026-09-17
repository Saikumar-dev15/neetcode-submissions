from typing import List

class Solution:
    nums = [1,2,3,3]
    def hasDuplicate(self, nums: List[int]):
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False