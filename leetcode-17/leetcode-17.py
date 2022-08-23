from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #固定数nums[k],用双指针在排序数组里找三数之和为-nums[k]
        nums.sort()
        numsPrototype = nums
        l = len(nums)
        res = []
        for k in range(l):
            tempt = numsPrototype[k]
            nums = numsPrototype[k+1:]
            for i, a in enumerate(nums):
                if i == 0 or nums[i] > nums[i - 1]:
                #开始双指针
                    left, right = i + 1, len(nums) - 1
                    while(left < right):
                        s = tempt + a +  nums[left] + nums[right]-target
                        if s == 0:
                            tmp = [numsPrototype[k],a, nums[left], nums[right]]
                            flag = 0
                            for item in res:
                                if tmp == item:
                                    flag = 1
                            if flag != 1:
                                res.append(tmp)
                            left += 1
                            right -= 1
                            while left < right and nums[left] == nums[left - 1]:
                                left += 1
                            while right > left and nums[right] == nums[right + 1]:
                                right -= 1
                        elif s < 0:
                            left += 1
                        elif s > 0:
                            right -= 1
        return res

nums = [2,2,2,2,2,2,2,2]
target = 8
print(Solution().fourSum(nums,target))