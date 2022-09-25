from typing import  List
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}  # 用字典进行存取
        for s in strs:  # 对每个字符串进行遍历
            keys = "".join(sorted(s))  # 对字符串进行正序排列
            if keys not in dic:  # 只有一个的情况
                dic[keys] = [s]  # 要记得带中括号，否则下面不能使用append()，而且最后的输出也需要。
            else:  # 多个的情况
                dic[keys].append(s)

        return list(dic.values())  # 只输出字典的值，并且转成列表格式。

nums: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(nums))