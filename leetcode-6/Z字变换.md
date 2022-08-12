#题目

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

**示例 1：**
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

**示例 2：**
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

**示例 3：**
输入：s = "A", numRows = 1
输出："A"

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#分析

这是一道找规律的题目。通过分析结构可以得到：
1. 每一个周期是**T = 2 x num - 2**个数，第一行和最后一行两个数之间的差值为**T**

2. 其余的行可以通过如下方式判断：首先，第一列肯定是从0到num-1，之后每一行的第一个数通过＋T的周期可以判断该行的下一个周期上是否有数。然后，分析结构，周期内的数可以通过下一个周期开头的数减去i来计算。
   
代码如下：

~~~python
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
~~~

#技术总结

1. 对continue的理解不深入。continue直接回到原循环，而无视后续的程序。
2. 此题充分地体现出一种分而治之、寻找锚点的过程，通过便于分析的数据为锚点去计算不便于分析的数，找出规律结合正确的逻辑，就不是难题。