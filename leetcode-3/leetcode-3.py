def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # 存储历史循环中最长的子串长度
    max_len = 0
    # 判断传入的字符串是否为空
    if s is None or len(s) == 0:
        return max_len
    # 定义一个字典，存储不重复的字符和字符所在的下标,字典的键（key）是字符，字典的值（value）是字符最后出现的index
    str_dict = {}
    # 存储每次循环中最长的子串长度
    one_max = 0
    # 记录最近重复字符所在的位置+1，or 设定头指针
    start = 0
    for i in range(len(s)):
        # 对于第一个字符，判断当前字符是否在字典中 & 当前字符的下标是否大于等于最近重复字符的所在位置
        # 如果字符在字典中，则说明重复了；如果字符下标索引的值str_dict[s[i]]>=start,说明在头指针右侧
        # if s[i] in str_dict and str_dict[s[i]] >= start:
        if s[i] in str_dict:
            # 记录当前字符的值+1
            start = str_dict[s[i]] + 1
            #start = start + 1

        #如果字符不在字典中则进行如下：
        # 在此次循环中，最大的不重复子串的长度
        one_max = i - start + 1
        # 把当前位置覆盖字典中的位置，记录该字符以及所在的index
        str_dict[s[i]] = i
        # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
        max_len = max(max_len, one_max)
    return max_len,str_dict

print(lengthOfLongestSubstring("pwwwkew"))
