class Solution:
        def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
            result = []
        
            for i,num in enumerate(nums):
                if num < 0:
                    num *= -1
                if nums[num-1] > 0:
                    nums[num-1] *= -1            

            for i,num in enumerate(nums):
                if num > 0:
                    result.append(i+1)

            return result
        