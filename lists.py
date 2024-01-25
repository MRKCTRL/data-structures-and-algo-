integ=[1,2,3,4]

string=['tue', 'wed', 'thurs']

mix=[1,2,1.5,'lenny', 1]

nest=[1,2,3,4[1.5, 15, 15], ['try']]

##################################################################

# acc/tr the list 

city=['cpt', 'jhb', 'pta']

city[1]

('jhb' in city)

for i in city:
    print(i)
    
for i in range(len(city)):
    city[i]=city[i]+"+"
    # empty list 

empty=[]
for a in empty:
    print('insert')
    
    
# update list 


lst=[1,2,3,5,56,48,48,6,9,84,9,4,898,4,8,48]
lst[2]=33
# time complexity:O(1)
# space complexity:O(1)

# insert list 
# insert(), append(), extend()

lst.insert(-1, 0) #--------->o(n)

lst.append(49) #--------->o(1)

lst1=[1,2,3,4,5,6]
lst.extend(lst1) #--------->o(n)

# space complexity:O(1)
# space complex:O(n)

# deletions in the list 
slice[:]
# fist and first and 3 index 
print(lst[0:2])

lst[0:2]= ['j', 'b']


lst.pop() #--------->o(n)/O(1)


del lst[2] #--------->o(n)
del lst[0:2] #--------->o(n)


lst.remove('e') #--------->o(n)

# space complexity:O(1)

# searching for an element in the a list 
# -in op 


if 20 in lst:
    print(lst.index(20)) #--------->o(n)
else: 
    print('the value does not exist')
    
# -linear search
def search(lst, value):
    for i in lst: #--------->o(n)
        if i == value: #--------->o(1)
            return lst.index #--------->o(1)
    return 'the value does not exist'
# time complexity:O(n)
# space complexity: O(1)
print(search(lst, 60))

# list op : fn 
a=[1,2,3]
b=[4,5,6]
c=a+b 


# * op 
a=[0,1]
a=a*4
print(a)

# len()
a[1,1,2,5,55,1,1,8,1561,56,15,171,]
len(a)

    
# max()
max(a)

# min()
min(a)

# sum()
sum(a)/len(a)

# total=0
# total=[]
# i can ust this for my wins and losses
total=list()
# count=0
while (True):
    inp=input('enter a number: ')
    if inp=='done':break
    value=float(inp)
    total.append(value)
    # total=total+value
    # count=count+1
average=sum(total)/len(total)
    # average=total/count
    
    
# strings and lists 
a='bam'
b=list(a)

# split()

a='hello hello hello'
dash='-'
b=a.split(dash)

# joint()
dash='-'
dash.join(b)


# stuff to avoid and avoid
lst=lst.sort()
orig=lst[:] 

myarray=np.array([1,2,4,3,5,6])
mylist=[1,2,3,4,5,6]