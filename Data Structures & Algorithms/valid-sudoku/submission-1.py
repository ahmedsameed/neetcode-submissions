class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        rset=set()
        cset=set()
        gset=set()


        for i in range(row):
            rset=set()
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rset:
                    return False
                rset.add(board[i][j])

        for j in range(col):
            cset=set()
            for i in range(row):
                if board[i][j] == ".":
                    continue
                if board[i][j] in cset:
                    return False
                cset.add(board[i][j])

        
        square = defaultdict(set)
        for i in range(row):
            for j in range(col):
                if board[i][j] == ".":
                    continue
                if board[i][j] in square[i//3,j//3]:
                    return False
                square[i//3,j//3].add(board[i][j])

        return True


        
