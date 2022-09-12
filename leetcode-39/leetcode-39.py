from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 结果列表
        ans = []
        # 可能的组合
        tmp = []

        def helper(idx, total):
            """回溯，求组合总和
            Args:
                idx: 选取元素索引
                total: 组合中的元素和
            """
            # 基准条件
            # 当元素和大于目标值，直接返回
            if total > target:
                return
            # 当元素和等于目标值，将组合添加到结果中，返回
            if total == target:
                ans.append(tmp[::])
                return

            # 进入分支，同时避免重复组合
            for i in range(idx, len(candidates)):
                # 更新 total 值，
                total += candidates[i]
                # 同时将当前元素尝试添加到组合中
                tmp.append(candidates[i])
                # 再次进入递归
                # 这里可以看文章图例，递归向下，可选元素是从自身开始选择
                # 这里同时也能避免组合重复，因为不会再次选择索引 i 前面对应的元素
                helper(i, total)
                # 回溯，回退组合元素及 total 值
                tmp.pop()
                total -= candidates[i]

        total = 0
        helper(0, total)
        return ans

num = [2,3,5]
target = 8

print(Solution().combinationSum(num,target))

