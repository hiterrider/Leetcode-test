class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]                            #设置一个列表，把该列表当做栈来使用即可。
        dic={')':'(','}':'{',']':'['}       #使用字典存储括号,并且右括号为key,左括号为value
        for char in s:
            if char in dic.values():        #左括号就入栈
                stack.append(char)
            elif char in dic.keys():        #有右括号的话就进行比较，
                if stack==[] or dic[char] != stack.pop():
                    return False
            else:
                return False                #不再字典中的输入直接输出错误

        return stack==[]                    #如果栈最后是空的，那么则符合要求，输出true,如果不是，则输出false,使用一个条件表达式

s = "()"
print(Solution().isValid(s))

