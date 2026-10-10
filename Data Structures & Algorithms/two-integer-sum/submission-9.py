class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}

        for i, num in enumerate(nums):
            second = target - num

            if second in seenDict:
                return [seenDict[second], i]

            seenDict[num] = i



        
        

        

            
                