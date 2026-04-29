class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining two numbers
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    # Skip duplicates for second number
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return result