class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        set_nums = set(nums)

        for n in set_nums:
            # Start only if n is the beginning of a sequence
            if n - 1 not in set_nums:
                length = 1
                current = n

                while current + 1 in set_nums:
                    current += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length