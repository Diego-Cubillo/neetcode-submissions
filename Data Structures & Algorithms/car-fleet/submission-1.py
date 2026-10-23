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

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for i, pos in enumerate(position):
            position[i] = (position[i], speed[i])

        position.sort()
        
        for i in range(len(position) - 1, -1, -1):
            pos, speed = position[i][0], position[i][1] 
            time = (target - pos) / speed
            if fleets:
                if time <= fleets[-1][0]:
                    fleets[-1][1] += 1
                else:
                    fleets.append([time, 1])
            else:
                fleets.append([time, 1])
                
        return len(fleets)