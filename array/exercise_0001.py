# 1. Two Sum
# https://leetcode.com/problems/two-sum
from typing import List

"""Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]"""

nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, element in enumerate(nums):
            complement = target - element
            if complement in seen:
                return [seen[complement], index]
            seen[element] = index
        return []
        
    
print(Solution.twoSum(Solution, nums, target))
