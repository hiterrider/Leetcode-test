from typing import  List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ##第一步，先对角线交换
        for i in range(n):
            for j in range(n-i):
                matrix[i][j],matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i],matrix[i][j]
        ##第二步，行变换
        # for i in range((n+1)//2):
        #         matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]



        return matrix

nums1: List[List[int]]= [[1,2,3],[4,5,6],[7,8,9]]
nums2: List[List[int]]= [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(Solution().rotate(nums1))