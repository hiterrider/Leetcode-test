from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums or n < 3:
            return None
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(0,n-2):
            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return target
                if abs(sum-target) < abs(res-target):
                    res = sum
                if sum < target:
                    l = l + 1
                else:
                    r = r - 1
        return res

nums = [-1,2,1,-4]

target = 1

print(Solution().threeSumClosest(nums,target))