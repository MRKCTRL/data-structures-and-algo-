def linearSearch(array, value):
    for i in range(len(array)):
        if array[i]==value:
            return i 
    return -1
    

linearSearch([2,1,5,5,1,5,8,4,58,17,56,1561,84,9,], 80)