class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checking = set()
        for num in nums:
            if num not in checking:
                checking.add(num)
            else:
                return True
        return False

        