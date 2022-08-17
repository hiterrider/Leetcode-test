class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if '' == str.strip():     #strip函数能够删除字符串的前后空格，若删除结束只有空格，则说明为0
            return 0
        sign, base, i = 1, 0, 0
        INT_MAX = 2147483647
        INT_MIN = -INT_MAX - 1
        while (str[i] == ' '):
            i += 1
        if str[i] == '-' or str[i] == '+':
            if str[i] == '-':
                sign = -1         #定义了一个符号
            i += 1

        while i < len(str) and '0' <= str[i] <= '9':
            if base > INT_MAX // 10 or base == INT_MAX // 10 and int(str[i]) > 7:  #此处值得借鉴，解决了之前发生的虚假判断溢出的问题
                return INT_MAX if sign == 1 else INT_MIN

            base = 10 * base + int(str[i])              #这是将单字符转化为数字的最关键迭代步骤，需要注意。
            i += 1

        return base * sign

s = Solution().myAtoi("        12sss34")