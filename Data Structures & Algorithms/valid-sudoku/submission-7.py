from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in board:
            row = Counter(i)
            row = dict(row)
            if "." in row.keys(): row["."] = 0
            if max(row.values()) > 1: return False
        visited = [0] * 9
        for i in range(9):
            visited = [0] * 9
            for j in range(9):
                print(visited[i])
                if board[j][i] != "." and visited[int(board[j][i])-1] == 1: return False
                if board[j][i] != ".": visited[int(board[j][i])-1] = 1
        visited = [0] * 9
        for i in range(0,9,3):
            for j in range(0,9,3):
                visited = [0] * 9
                for m in range(3):
                    for n in range(3):
                        
                        if board[m+i][n+j] != "." and visited[int(board[m+i][n+j])-1] == 1: return False
                        if board[m+i][n+j] != ".": visited[int(board[m+i][n+j])-1] = 1
        return True

