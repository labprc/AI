def is_safe(board,row, col, n):
    for i in range(row):
        if board[i][col]==1:
            return False
    
    i,j=row-1,col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    i,j=row-1,col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1

    return True

def solve_nqueen(board,row,n):
    if row==n:
        print_board(board,n)
        return
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col]=1
            solve_nqueen(board,row+1,n)
            board[row][col]=0#backtracking

def print_board(board,n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j]==1 else ".", end=" ")
        print()
    print()

n=4
board=[[0]*n for i in range(n)]
solve_nqueen(board,0,n)