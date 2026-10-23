class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1

        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1

        for key, value in sDict.items():
            if key in tDict:
                if value != tDict[key]:
                    return False
            else:
                return False

        return len(sDict) == len(tDict)