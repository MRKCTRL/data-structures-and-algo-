activities=[['a1', 0, 6],
            ['a1', 3,4 ],
            ['a3', 1, 3],
            ['a4', 5, 4],
            ['a5', 5, 8],
            ['a6', 8,9]
            ]

def printMaxActivites(activites):
    activites.sort(key=lambda x:x[2])
    i=0
    firstA=activites[i][0]
    print(firstA)
    for j in range(len(activites)):
        if activites[j][1]>activites[i][2]:
            print[activities[j][0]]
            i=j
    
printMaxActivites(activites)