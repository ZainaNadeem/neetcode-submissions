class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            answer = ''.join(sorted(word))
            if answer not in dic:
                dic[answer] = []
            dic[answer].append(word)

        result = []
        for values in dic.values():
            result.append(values)

        return result

        