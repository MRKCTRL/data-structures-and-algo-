class Item:
    def __init__(self, weight, value):
        self.weight=weight
        self.value=value
        self.ratio=value/weight
        
def knapsackMethod(items, capacity ):
    items.sort(ley=lambda x:x.ratio, reverse=True)
    usedCap=0
    totalVal=0
    for i in items:
        if usedCap +i.weight<=capacity:
            usedCap +=i.weight
            totalValue+=i.value
        else:
            unusedweight=capacity-usedCap
            value=i.ratio * unusedweight
            usedCap+=unusedweight
            totalValue+=value
        if usedCap==capacity:
            break
    print('total value obtained: '+str(totalValue))
    
    item1=Item(20,100)
    item=Item(30,120)
    item3=Item(10,60)
    cList=[item1, item, item3]
        