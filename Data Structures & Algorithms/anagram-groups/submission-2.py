class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myWords = {}
        
        for myStr in strs:
            frequency = [0] * 26

            for char in myStr:
                frequency[ord(char.lower()) - ord("a")] += 1
            
            myTup = tuple(frequency)

            if myTup in myWords:
                myWords[myTup].append(myStr)
            else:
                myWords[myTup] = [myStr]
                    

        return list(myWords.values())
            
                
            