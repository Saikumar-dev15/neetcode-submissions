class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for i in store:
            if i - 1 not in store:
                streak , curr = 0, i
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res


