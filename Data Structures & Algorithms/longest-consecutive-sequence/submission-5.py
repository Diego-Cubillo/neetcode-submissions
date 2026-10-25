class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxSeq = 0

        for num in numsSet:
            if num - 1 not in numsSet:
                currNum = num
                currSeq = 1

                while currNum + 1 in numsSet:
                    currNum += 1
                    currSeq += 1

                maxSeq = max(maxSeq, currSeq)

        return maxSeq

"""
[2,20,4,10,3,4,5]
[2,3,4,4,5,10,20]
"""