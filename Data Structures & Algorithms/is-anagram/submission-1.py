class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        for letter in s:
            dic[letter] = dic.get(letter, 0) + 1
        for letterr in t:
            dic[letterr] = dic.get(letterr, 0) - 1
        
        for values in dic.values():
            if values != 0:
                return False
        return True
        
        