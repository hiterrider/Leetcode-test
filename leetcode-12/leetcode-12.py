# class Solution:
#     def romanToInt(self, s: str) -> int:
        # list1=[900,400,90,40,9,4]
        # list2=['CM','CD','XC','XL','IX','IV']
        # list3=[1000,500,100,50,10,5,1]
        # list4=['M','D','C','L','X','V','I']
        # s = list(s)
        # result = 0
        #
        # for i in range(len(list2)):
        #     for j in range(len(s)-1):
        #         if s[j]+s[j+1] == list2[i]:
        #             result = result + list1[i]
        #             s[j] = 'Null'
        #             s[j+1] = 'Null'
        #             # s = s.replace(s[j],'+')
        #             # s = s.replace(s[j+1], '+')
        #
        # for i in range(len(list4)):
        #     for j in range(len(s)):
        #         if s[j] == list4[i]:
        #             result = result + list3[i]
        #
        # return  result , s

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans=0
        for i in range(len(s)):
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans

s = "MCMXCIV"
print(Solution().romanToInt(s))