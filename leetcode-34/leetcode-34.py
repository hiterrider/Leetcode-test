from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binsear_right(nums, tar):  # 找右边界，mid在右区间
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
                return -1

        def binsear_left(nums, tar):  # 找左边界，mid在左区间
            low, high = 0, len(nums) - 1
            while low < high:
                mid = (low + high) // 2  # 下取整
                if nums[mid] >= tar:
                    high = mid
                else:
                    low = mid + 1
            if nums[low] == tar:
                return low
            else:
                return -1

        if len(nums) == 0: return [-1, -1]
        left_idx = binsear_left(nums, target)
        if left_idx == -1: return [-1, -1]  # 没有左边界亦无右边界。
        right_idx = binsear_right(nums, target)
        return [left_idx, right_idx]

nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums,target))


