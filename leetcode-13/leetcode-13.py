from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''	# 定义空字符串，准备用来存放最长公共子串
        for tuples in zip(*strs):	# *strs 将列表解包成几个字符串元素
            if len(set(tuples)) == 1:	# 判断zip后的元素的集合的长度，如果=1，
                                    # 说明几个字母相等，追加到最长公共子串中
                ans += tuples[0]
            else:					# 否则就是不相等。
                break
        return ans

s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))


str1 = ["flower", "flow", "flight"]
for tuple in zip(*str1):
    print(tuple)