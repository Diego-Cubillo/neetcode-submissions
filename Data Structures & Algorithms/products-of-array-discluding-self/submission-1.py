class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonZeroTotal = None
        zero = False

        for num in nums:
            if num != 0:
                if nonZeroTotal == None:
                    nonZeroTotal = num
                else:
                    nonZeroTotal *= num
            else:
                if zero:
                    nonZeroTotal = 0
                    break

                zero = True
    
        output = []

        for num in nums:
            if num != 0:
                if zero:
                    result = 0
                else:
                    result = nonZeroTotal // num
            else:
                result = nonZeroTotal
            output.append(result)
    
        return output