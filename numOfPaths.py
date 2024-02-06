def numOfPath(twoDArray, row, col, cost):
    if cost<0:
        return 0
    elif row==0 and col==0:
        if twoDArray[0][0]-cost =0:
            return 1 
        else:
            return 0
    elif row==0:
        return numOfPath(twoDArray, 0,col-4,cost-twoDArray[row][col])
    elif col==0:
        return numOfPath(twoDArray, row-1, col-1, cost, twoDArray[row][col])
    else:
        op1=numOfPath(twoDArray, row-1,col,cost-twoDarray[row][col])
        op2=numOfPath(twoDArray, row,col-1,cost-twoDarray[row][col])
        return op1 + op2
    

        