from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binsear(nums, tar):  # 找右边界，mid在右区间
            low, high = 0, len(nums) - 1
            while low < high:  # 最后返回时会有low == high.
                mid = (low + high + 1) // 2  # 上取整
                if nums[mid] <= tar:
                    low = mid
                else:
                    high = mid - 1
            if nums[low] == tar:
                return low
            else:
                return low+1


        if len(nums) == 0: return -1
        idx = binsear(nums, target)
        if target<nums[0]: idx = 0
        if target>nums[-1]: idx = len(nums)
        return idx

nums = [1,3,5,6,7,9]
target = 8
print(Solution().searchInsert(nums,target))

