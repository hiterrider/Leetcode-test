from typing import  List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        tem = []

        def backtrack(nums, tem):
            if nums == []:
                if tem not in res:
                    res.append(tem[:])
            else:
                for i in range(len(nums)):
                    tem.append(nums[i])
                    backtrack(nums[0:i] + nums[i + 1:], tem)
            if tem == []:
                return 0
            tem.pop()

        backtrack(nums, tem)
        return res

nums: List[int] = [1,2,3]
print(Solution().permute(nums))