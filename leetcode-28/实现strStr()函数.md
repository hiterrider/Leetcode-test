##题目

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 
**示例 1：**
输入：haystack = "hello", needle = "ll"
输出：2

**示例 2：**
输入：haystack = "aaaaa", needle = "bba"
输出：-1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


~~~python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == []:
            return 0

        if len(needle)>len(haystack):
            return -1

        for i in range(len(haystack)):
            j = 0
            if needle[j] == haystack[i]:
                k = i
                while j < len(needle):
                    if needle[j] == haystack[k]:
                        j = j + 1
                        k = k + 1
                    else:
                        break
            if j == len(needle):
                return i

        return -1

haystack = "mississippi"
needle = "issip"
print(Solution().strStr(haystack,needle))
~~~

~~~python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        l1 = len(haystack)
        l2 = len(needle)
 
        if l1 < l2:
            return -1
 
        l = l1 - l2 + 1
        for i in range(l):
            if haystack[i:i+l2] == needle:
                return i
        return -1
~~~

采用了两种方法，但是第一种方法能在本地编译器上运行，在leetcode上则会出现超出数组边界的错误，目前尚不清楚原因。第二种方法相对讨巧，本题如果不用暴力枚举的方法，就是复杂的KMP问题。而第二题直接利用python自带的功能实现了，不可不谓剑走偏锋。