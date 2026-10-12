class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1,len(nums)+1))
        missing = list(all_nums - set(nums))
        return missing