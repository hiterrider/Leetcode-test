# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#实例：

# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/two-sum

#最简单的算法，暴力加和
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if len(nums) < 2:
#             return
#         for i in range(0, len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#采用哈希表的方法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict0 = {}          #定义一个空哈希表
        for i in range(0, len(nums)):  #遍历数组
            num = target - nums[i]     #判断当前指针所指位置的数的补
            if num not in dict0:       #判断补是否在哈希表内
                dict0[nums[i]] = i     #如果不在，则将当前的数值和位置存入表中
            else:
                return [dict0[num], i] #如果在，则直接输出当前位置和补的位置

