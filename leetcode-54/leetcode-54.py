from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return []
        m,n = len(matrix),len(matrix[0])
        x = y = di = 0
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        res = []
        visited = set()

        for i in range(m*n):
            res.append(matrix[x][y])
            visited.add((x,y))
            nx,ny = x+dx[di],y+dy[di]
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                x,y = nx,ny
            else:
                di = (di+1)%4  # 如果不满足条件，换一个方向进行遍历
                x,y = x+dx[di],y+dy[di]
        return res



matrix:List[int] = [[1,2,3],[4,5,6],[7,8,9]]

print(Solution().spiralOrder(matrix))