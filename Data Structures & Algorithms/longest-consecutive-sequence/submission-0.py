class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Convert array to set -> Fast loop up
                            # ->Removes Duplicate
        numSet = set(nums)
        longest = 0

        #Check if n is the beginning of the sequence
        #It is not the beginning if n-1 exists
        for n in nums:
            if (n-1) not in numSet:
                #Start checking the sequence
                #As you find the sequence you increment the length
                length = 0
                while (n+length) in numSet:
                    length += 1
                #At each iteration, find the next larger number in the sequence
                #when the sequence breaks, you store the length to compare
                longest = max(length, longest)

        return longest


        