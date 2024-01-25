from array import * 

# create and travse
myArray=array('i', [1,2,3,4,5,6])

for i in myArray:
    print(i)
    

# access indi elements through index 

print(myArray[0])


# append any value to array ysing append() method
myArray.append(7)


# insert val in an array using insert() method
myArray.insert(0,11)

# extend a python array using extend() method

array2 = array('i', [10,.11,12,])
array.extend(array2)

# add items from the list into array ysung fromlist() method 
templist=[1,2,3,4,5]
myArray.fromlist(templist)


# fromve any array element using remove()
templist=[1,2,3,4,5]
myArray.remove(5)

# remove last element using pop()
templist=[1,2,3,4,5]
myArray.pop()

# fetch any element through index using index() method
templist=[1,2,3,4,5]
myArray.index(21)

# reverse python array using reverse() method

myArray.reverse()


# get array buffer info through buffer info() method 
myArray.buffer_info()


# check for number of uccurences of an element using count() method 

myArray.count(1)

# convert array to string using tostring() method 
strtemp=myArray.tostring()

ints = array('i')
int.fromstring(strtemp)

# covert array to python list with same using same elements tolist() method 
myArray.tolist()


# append a string to char using fromstring() method 


# slice elments from an array 
myArray[1:4]