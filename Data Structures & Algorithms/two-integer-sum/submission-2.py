class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            goal_num = target - nums[i]
            if goal_num in nums[i+1:]:
                return [i, nums[i+1:].index(goal_num) + i + 1]
        