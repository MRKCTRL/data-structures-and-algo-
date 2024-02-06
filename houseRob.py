def houseRob(houses, currentIndex):
    if currentIndex>=len(houses):
        return 0
    else:
        stealFirstHouse=houses[currentIndex]+houseRob(houses, currentIndex+2)
        skipFirstHouse=houseRob(houses, currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)
        