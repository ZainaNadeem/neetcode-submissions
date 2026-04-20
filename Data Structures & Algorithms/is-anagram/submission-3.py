class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Let's create a dictionary to keep track of the appearance of
        # letters in one word
        # Then we increment the value as the letters appear in string s
        # Then we decrement the value as the letters appear in string t

        # Base Case: Un-equal length
        if len(s) != len(t):
            return False

        dic = {}
        for letter in s:
            dic[letter] = dic.get(letter, 0) + 1
        for letter_t in t:
            dic[letter_t] = dic.get(letter_t, 0) - 1

        for values in dic:
            if dic[values] != 0:
                return False
        return True



        