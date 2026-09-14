class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check row
        for i in range(9):
            read = set()
            for n in board[i]:
                if n in read: return False
                if n != ".": read.add(n)
        
        #check col
        for c in range(9):
            read = set()
            for r in range(9):
                n = board[r][c]
                if n in read: return False
                if n != ".": read.add(n)

        #check 9x9
        read=set()
        for n in board[0:3]:
            for m in n[0:3]:
                if m in read: return False
                if m != ".": read.add(m)

        read.clear()
        for n in board[0:3]:
            for m in n[3:6]:
                if m in read: return False
                if m != ".": read.add(m)
        read.clear()
        for n in board[0:3]:
            for m in n[6:9]:
                if m in read: return False
                if m != ".": read.add(m)
        read.clear()
        for n in board[3:6]:
            for m in n[0:3]:
                if m in read: return False
                if m != ".": read.add(m)
        read.clear()
        for n in board[3:6]:
            for m in n[3:6]:
                if m in read: return False
                if m != ".": read.add(m)
        read.clear()
        for n in board[3:6]:
            for m in n[6:9]:
                if m in read: return False
                if m != ".": read.add(m)
        
        read.clear()
        for n in board[6:9]:
            read = set()
            for m in n[0:3]:
                if m in read: return False
                if m != ".": read.add(m)

        read.clear()
        for n in board[6:9]:
            for m in n[3:6]:
                if m in read: return False
                if m != ".": read.add(m)
        
        read.clear()
        for n in board[6:9]:
            for m in n[6:9]:
                if m in read: return False
                if m != ".": read.add(m)

        return True
