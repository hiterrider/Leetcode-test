from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(prefix, left, right):
            if len(prefix) == 2 * n:
                res.append(prefix)
                return
            # 控制左括号的数量，避免出现'(((((('的情况
            if left < n:
                backtrack(prefix + '(', left + 1, right)
            # 控制右括号的数量
            if right < left:
                backtrack(prefix + ')', left, right + 1)
        backtrack('', 0, 0)
        return res

n = 3
print(Solution().generateParenthesis(n))