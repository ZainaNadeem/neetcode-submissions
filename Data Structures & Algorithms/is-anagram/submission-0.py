class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        track = {}
        for letter in s:
            track[letter] = track.get(letter, 0) + 1
        for lette in t:
            track[lette] = track.get(lette, 0) - 1

        for value in track.values():
            if value != 0:
                return False

        return True
        

        
