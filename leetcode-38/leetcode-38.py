class Solution:
    def countAndSay(self, n: int) -> str:
        def Handle(item):
            p = 0            # 游标 指向元素
            res = ''          # 用来存放生成的答案
            while p < len(item):   # 当 p 不超出item长度
                count = 1         # 记录相同数字的数量
                # 当 p 还没到最后一个元素，且与下一个元素相同
                while p < len(item) - 1 and item[p] == item[p+1]:
                    count += 1     # 数量+1
                    p += 1       # 游标指向下一位
    # 如果上面的while执行了，就把信息存放，否则表示跟前一个&下一个元素不同，将初始值1存放
                res += str(count) + item[p]
                p += 1
            return res
        res = '1'
        for i in range(1, n):
            res = Handle(res)
        return res

print(Solution().countAndSay(5))