from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        numsLength = len(nums)
        front = 0
        back = numsLength-1
        index = -1

        while front <= back :
            if nums[front] == target:
                index = front
                break
            if nums[front] > target:
                if nums[back] == target:
                    index = back
                    break
                if nums[back] > target:
                    back = back - 1
                if nums[back] < target and front < back:
                    return -1
            if nums[front] < target:
                front = front + 1

        return index

nums = [6,5,4,0,1,2]
target = 3
print(Solution().search(nums,target))