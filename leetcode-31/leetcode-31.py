class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                flag= nums[i]
                flag_i = i
                nums[i:] = sorted(nums[i:])
                for j in range(i+1,len(nums)):
                    if nums[j]>nums[i-1] and nums[j]<=flag:
                        flag = nums[j]
                        flag_i = j
                nums[i-1],nums[flag_i]=nums[flag_i],nums[i-1]
                nums[i+1:] = sorted(nums[i+1:])

                return nums
        nums.sort()
        return nums

nums=[1,2,3]
print(Solution().nextPermutation(nums))