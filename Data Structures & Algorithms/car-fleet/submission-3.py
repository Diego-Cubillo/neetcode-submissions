class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for i, pos in enumerate(position):
            position[i] = (position[i], speed[i])

        position.sort()
        
        for i in range(len(position) - 1, -1, -1):
            pos, speed = position[i][0], position[i][1] 
            time = (target - pos) / speed
            if fleets:
                if time <= fleets[-1]:
                    continue
                else:
                    fleets.append(time)
            else:
                fleets.append(time)
                
        return len(fleets)