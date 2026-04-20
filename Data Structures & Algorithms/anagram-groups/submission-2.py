class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            structured_word = "".join(sorted(word))
            if structured_word in dic:
                dic[structured_word].append(word)
            else:
                dic[structured_word] = [word]

        lyst = []
        for values in dic.values():
            lyst.append(values)

        return lyst
        



        