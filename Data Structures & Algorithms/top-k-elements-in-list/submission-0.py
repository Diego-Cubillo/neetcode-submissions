class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        myTups = []

        for item, freq in freq.items():
            myTups.append((freq, item))

        myTups.sort()
        selected = []

        for index, (freq, item) in enumerate(myTups[::-1]):
            if index == k:
                break
            else:
                selected.append(item)

        return selected