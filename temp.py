

numday=int(input('how many days temp'))
total=0
temp=[]
for i in range(numday):
    nextday=input(f'day {i+1} high temp:')
    temp.append(nextday)
    total += temp[i]
avg=round(total/numday,2)
print(f'\nAverage str{avg}')

above=0 
for i in temp:
    if i>avg:
        above+=1
print(f'{above} days above average')