tup=('j','t','j','f','f','f','dfv','ffs','fd')

tup2=('a',)

tup3=tuple('gyufguyftfyvghigbygyolgtygftftyuouyg')

# time space:O(1)
# space complexity :O(n)

tup[3]
tup[:]

# def search()
for i in tup:
    print(i)
    
    
for i in range(len(tup)):
    print(tup[i])
    # time space:O(n)
# space complexity :O(1)


print('b' in tup)

def srchtup(tup, element):
    for i in tup: #---------->O(n)
        if i == element: #---------->O(1)
            return tup.index(i) #---------->O(1)
    return 'the element does exist' #---------->O(1)

# time space:O(n)
# space complexity :O(1)

srchtup()

combo=tup+tup3
tup*6
tup.count(2)
tup.index()
len(tup)
min(tup)
max(tup)


# tuples vs lists
lst=[1,2,3,4,5,6]

lst[1]=3


tup1='j','t','j','f','f','f','dfv','ffs','fd'