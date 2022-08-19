# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         cap_max =0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#
#                 if j>i:
#                     cap = min(height[i],height[j])*(j-i)
#                     cap_max = max(cap_max,cap)
#
#         return cap_max

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=l=0
        r=len(height)-1
        while l<r:
            res=max(res,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res