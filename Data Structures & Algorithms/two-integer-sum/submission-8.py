class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        reminder = None
        selectedNum = None

        for index, num in enumerate(nums):
            reminder = target - num

            if reminder in seen:
                return [seen[reminder], index]
            else:
                seen[num] = index
