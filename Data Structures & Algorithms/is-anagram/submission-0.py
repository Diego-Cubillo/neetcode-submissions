class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        net_count = {chr(ord('a') + i): 0 for i in range(26)}

        for i in s:
            net_count[i] +=  1
        
        for i in t:
            net_count[i] -= 1

        for value in net_count.values():
            if value != 0:
                return False
        
        return True