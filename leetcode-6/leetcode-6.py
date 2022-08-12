class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        end = ''
        n = len(s)
        if numRows <= 1:
            return s
        T = numRows * 2 - 2
        res = ""  #定义一个空字符串
        for i in range(numRows):
            cnt = 0
            while (1):
                if cnt * T + i < len(s):  #分析结构可知，0~num-1的数据必然在第一列
                    res += s[cnt * T + i]
                    print(res)
                else:
                    break
                if i == 0 or i == T / 2:
                    cnt += 1
                    continue
                if cnt * T + T - i < len(s):
                    res += s[cnt * T + T - i]
                else:
                    break
                cnt += 1
        return res

num = 4
s = "abcdef"
s2 = Solution().convert(s,num)
print(s2)
