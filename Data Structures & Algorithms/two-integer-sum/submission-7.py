class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        reminder = None
        selectedNum = None

        for num in nums:
            reminder = target - num

            if reminder in seen:
                selectedNum = num
                break
            else:
                seen.add(num)

        index1 = None
        index2 = None
        print(reminder, selectedNum)
        for i, num in enumerate(nums):
            if num == reminder or num == selectedNum:
                if index1 == None:
                    index1 = i
                else:
                    index2 = i

        return [index1, index2]
