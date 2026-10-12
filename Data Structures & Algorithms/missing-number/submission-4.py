class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        all_nums = list(range(0,n+1))
        missing = set(all_nums) - set(nums)
        return missing.pop() #if missing else None