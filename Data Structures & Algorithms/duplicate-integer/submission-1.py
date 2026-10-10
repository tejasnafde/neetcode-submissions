class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set()
        for num in nums:
            if num not in unique_vals:
                unique_vals.add(num)
            else:
                return True
        return False

            