class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        myDictSpeed = {}
        for i, pos in enumerate(position):
            myDictSpeed[pos] = speed[i]

        position.sort()
        
        for i in range(len(position) - 1, -1, -1):
            pos = position[i]
            time = (target - pos) / myDictSpeed[pos]
            if fleets:
                if time <= fleets[-1][0]:
                    fleets[-1][1] += 1
                else:
                    fleets.append([time, 1])
            else:
                fleets.append([time, 1])
        return len(fleets)