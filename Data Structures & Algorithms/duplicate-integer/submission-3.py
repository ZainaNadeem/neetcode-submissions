class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        remove_dups = set()

        for n in nums:
            if n in remove_dups:
                return True
            else:
                remove_dups.add(n)
        return False
        