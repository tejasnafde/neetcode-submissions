class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,num in enumerate(nums):
            if num in dict1.keys() and dict1.get(num) != i:
                return [dict1.get(num), i]
            dict1[(target - num)] =  i # required index of j for this 1
            
                
                # [4,5,6]

                # {
                #     5: 0,
                #     
                # }
            
        

        

            
                