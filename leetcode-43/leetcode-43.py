class Solution:
    def mul(self,num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]  # 字符串反转，如果是list反转，则用list.reverse()，从最后一位开始模拟手算
        num2 = num2[::-1]
        len_all = len(num1) + len(num2)
        result = [0 for i in range(len_all)]   #保存一个结果的数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += int(num1[i]) * int(num2[j])  #将每位数字相乘的结果写入数组保留
        for i in range(len_all):
            if result[i] > 9:                                 #计算进位
                result[i + 1] += result[i] // 10
                result[i] = result[i] % 10
        result.reverse()                                      #翻转
        resu = "".join(str(result[i]) for i in range(len(result)))  #转化为字符串
        res = str(int(resu))  # 去掉前面的0
        return  res


num1 = '98'
num2 = '43'
print(Solution().mul(num1,num2))