class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        currSeq = 0

        nums.sort()

        i = 0
        while i < len(nums):

            currNum = nums[i]
            currSeq += 1  

            if i + 1 >= len(nums) or  (currNum + 1 != nums[i+1] and currNum != nums[i+1]):
                if currSeq > maxSeq:
                    maxSeq = currSeq 
                currSeq = 0
            else:
                if currNum == nums[i+1]:
                    currSeq -= 1    

            i += 1
        
        return maxSeq

"""
[2,20,4,10,3,4,5]
[2,3,4,4,5,10,20]
"""