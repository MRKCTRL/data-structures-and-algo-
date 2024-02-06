def houseRobberTD(houses, currentIndex, tempDict):
    if currentIndex>=len(houses):
        return 0
    else:
        if currentIndex not in tempDict:
            stealFistHouse=houses[currentIndex]+houseRobberTD
            skipFirstHouse=houseRobberTD(houses, currentIndex+1, tempDict)
            tempDict[currentIndex]=max(stealFistHouse, skipFirstHouse)
        return tempDict[currentIndex]
    
houses =[6,7,1,30,8,2,4]

def houseRobberBU(houses, currentHouse):
    tempArr=[0]*(len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        tempArr[i]=max(houses[i]+tempArr[i+2], tempArr[i+1])
    return tempArr[0]


