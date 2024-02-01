import math 

def binarySearch(array, value):
    start=0
    end=len(array)-1
    middle=math.floor(start+end)/2
    print(start, middle,end)
    while not(array[middle]==value):
        if value <array[middle]:
            end=middle-1
        else:
            start=middle+1
        middle=math.floor((start+end)/2)
        print(start, middle, end)
        
    return middle 
    
custARRAY=[1,55,51,51,5,47164,165,1]