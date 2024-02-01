def numFactor(n):
    if n in (0,1,2):
        return 
    elif n==3:
        return 2 
    else:
        subP=numbFactor(n-1)
        subP2=numFactor(n-1)
        subP3=numbFactor(n-4)
        return subP+subP2+sub3