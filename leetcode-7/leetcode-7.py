class Solution:
    def reverse(self, x: int) -> int:

        y = 0
        if x<0:
            x = -x
            while(x!=0):
                y = y*10 + x%10
                x = x//10
            y = -y
        else:
            while (x!=0):
                y = y * 10 + x % 10
                x = x // 10
        if y > pow(2, 31) - 1 or y < pow(-2, 31):
            return 0
        return y


print(Solution().reverse(-1234567))