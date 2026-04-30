class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for z in t:
            dic[z] = dic.get(z, 0) - 1

        for r in dic.values():
            if r != 0:
                return False
        return True
        