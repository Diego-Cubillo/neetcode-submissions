class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        myBucks = [[] for _ in range(len(nums) + 1)]

        for num, value in freq.items():
            myBucks[value].append(num)

        selected = []
        count = 0

        for buck in myBucks[::-1]:
            for num in buck:
                selected.append(num)  
                count += 1
                if count == k:
                    return selected
                        