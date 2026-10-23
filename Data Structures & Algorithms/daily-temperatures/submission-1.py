class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        waiting = []

        for i, temp in enumerate(temperatures):
            while waiting and temp > waiting[-1][0]:
                day = waiting.pop()[1]
                output[day] = i - day

            waiting.append((temp, i))

        return output