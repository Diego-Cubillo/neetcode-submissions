class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))]
        waiting = []

        for i, temp in enumerate(temperatures):
            while len(waiting) > 0 and temp > waiting[-1][0]:
                hTemp, day = waiting.pop()
                output[day] = i - day

            waiting.append((temp, i))

        return output
"""
temperatures = [30,38,30,36,35,40,28]

i = 0
output = []
waiting = [(30, 0)]

i = 1
output = [1]
waiting = [(38, 1)]

i = 2
output = [1]
waiting = [(38, 1), (30, 2)]

i = 3
output = [1]
waiting = [(38, 1), (30, 2)]

"""