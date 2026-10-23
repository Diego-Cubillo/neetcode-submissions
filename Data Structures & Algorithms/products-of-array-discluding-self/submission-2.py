class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preResults = {}
        sufResults = {}

        for i, num in enumerate(nums):
            if i - 1 >= 0:
                preResults[i] = preResults[i-1] * num
            else:
                preResults[i] = num
        
        i = len(nums) - 1
        while i >= 0:
            if i + 1 < len(nums):
                sufResults[i] = sufResults[i+1] * nums[i]
            else:
                sufResults[i] = nums[i]
            i -= 1

        output = []
        for i, num in enumerate(nums):
            if i == 0:
                result = sufResults[i+1]
            elif i == len(nums) - 1:
                result = preResults[i-1]
            else:
                result = preResults[i-1] * sufResults[i+1]
            output.append(result)
        
        return output