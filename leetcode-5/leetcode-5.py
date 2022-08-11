class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 以[left,right]为中心不断外扩, 找到回文子串.
        def help(s, left, right):
            N = len(s)
            while left >= 0 and right < N and s[left] == s[right]:
                left -= 1
                right += 1
            # 返回回文子串的长度
            return right - left - 1

        if not s:
            return ""
        start, end = 0, 0

        for i in range(len(s)):
            # 注意: "abba"和"aba"两种情况
            len1, len2 = help(s, i, i), help(s, i, i + 1)
            len0 = max(len1, len2)
            # 找到回文子串的起始~终止索引
            if len0 > end - start:
                start = i - (len0 - 1) // 2
                end = i + len0 // 2
            print(s[start:end + 1])
        return s[start:end + 1]

s = "abcdcbb"
Solution().longestPalindrome(s)