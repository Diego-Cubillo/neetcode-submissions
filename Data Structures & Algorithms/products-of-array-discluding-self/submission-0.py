class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = None
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
                    total = 0 
                    break

                zero = True
        
            if total == None:
                total = num
            else:
                total *= num

        output = []
        print(total)
        print(nonZeroTotal)

        for num in nums:
            if num != 0:
                result = total // num
            else:
                result = nonZeroTotal
            output.append(result)
    
        return output