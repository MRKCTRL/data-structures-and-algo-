import numpy as np 

twoDArray=np.array([9, 10, 11, 12], [13,14,15], [16, 17, 18, 19], [20, 21, 22, 23]) #------>0(1)


twooArr=np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1) #or axis=0


twooArr=np.append(twoDArray, [[1, 2, 3, 4]], axis=0) 


def accessEL(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): #------------->O(1)
        print(' incorrect index ') #------------->O(1)
    else:
        # this is a 2d array rather written like a[i][c] the below is the same to give description 
        array[rowIndex][colIndex] #------------->O(1)
        # space complexity :O(1)
accessEL(twoDArray, 2,3)

def travis(array):
    for i in range(len(array)): #------------->O(mn)
        for j in range(len(array[0])):#------------->O(n)
            print(array[i][j])#------------->O(1)
            # O(n^2) space complexity:O(1)
            
travis(twoDArray)


def searchEl(array, value):
    for i in range( len(array)): #------------->O(mn)
        for j in range(len(array[0])): #------------->O(n)
            if array[i][j] == value: #------------->O(1)
                return 'the value is located at index' +str(i)+ ""+str(j)
    return 'element not found'
#o(mn) space complexity O(1)


searchEl(twoDArray, 14)
newTdArray=np.delete(twoDArray, 0, axis=0) #------------->O(1)
# space complexity:O(1)