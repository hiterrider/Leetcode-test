from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def helper(i,cur_sum,ans):
            if cur_sum == target:
                res.append(ans)
                return
            if i == n or cur_sum > target:
                return
            for j in range(i, n):
                if j!=i and candidates[j] == candidates[j-1]: ##如果重复则跳过
                    continue
                if cur_sum + candidates[j] > target:
                    break
                helper(j + 1, cur_sum + candidates[j], ans + [candidates[j]])

        helper(0, 0, [])
        return res


num = [10,1,2,7,6,1,5]
target = 8

print(Solution().combinationSum2(num,target))

