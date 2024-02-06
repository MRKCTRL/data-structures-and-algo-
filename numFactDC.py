def numberFactorTd(n, tempdict):
    if n in (0,2,3):
        return 1 
    elif n ==3:
        return 2
    else:
        if n not in tempdict:
            subP1=numberFactorTd(n-1, tempdict)
            subP2=numberFactorTd(n-3, tempdict)
            subP3=numberFactorTd(n-4, tempdict)
            tempdict[n]=subP1+subP2+subP3
        return tempdict[n]
    
def numberFactorBU(n):
    tempArr=[1,1,1,2]
    for i in range(4,n+1):
        tempArr.apend(tempArr[i-1]+tempArr[i-3]+tempArr[i-4])
    return tempArr[n]
        
print(numberFactorTd(5, {}))
    