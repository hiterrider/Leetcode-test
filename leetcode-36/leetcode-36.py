from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 逐行检查
        for i in range(9):
            # 存储每行出现的数字字符
            storage = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])

        # 逐列检查
        for i in range(9):
            # 存储每列出现的数字字符
            storage = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in storage:
                    return False
                else:
                    storage.append(board[j][i])

        # 检查九宫格
        # 每个九宫格的开始索引
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                storage = []
                # 遍历3X3格子中字符
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] == ".":
                            continue
                        if board[i + x][j + y] in storage:
                            return False
                        else:
                            storage.append(board[i + x][j + y])
        # 全部检查通过
        return True

