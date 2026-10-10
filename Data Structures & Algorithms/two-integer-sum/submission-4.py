class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        # diff = 0
        for i,num in enumerate(nums):
            difference = target - nums[i]
            if difference not in diff_dict.keys():
                diff_dict[num] = i
            else:
                return [diff_dict.get(difference), i]

            
                