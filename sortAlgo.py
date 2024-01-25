import math
def Bs(customlist):
    for i in range(len(customlist)-1):
        for j in range(len(customlist)-i-1):
            if customlist[j]>customlist[j+1]:
                customlist[j], customlist[j+1]=customlist[j+1], customlist[j]         
    print(customlist)
    
def selectionSort(customlist):
    for i in range(len(customlist)):
        minIndex=i
        for j in range(i+1, len(customlist)):
            if customlist[minIndex] > customlist:
                minIndex=j 
        customlist[i], customlist[minIndex]=customlist[minIndex], customlist[i]
    print(customlist)


def insertionSort(customlist):
    for i in range(1, len(customlist)):
        key=customlist[i]
        k=i-1
        while j>=0 and key<customlist[j]:
            customlist[k+1]=customlist[j]
            j-=1
            customlist[j+1]=key
    print(customlist)

def bucketSort(customlist):
    numOfBuckets=round(math.sqrt(len(customlist)))
    maxValue=max(customlist)
    arr=[]
    for i in range(numOfBuckets):
        arr.append([])
    for j in customlist:
        indexB=math.ceil(j*numOfBuckets/maxValue)
        arr[indexB-1].append(j)
    
    for i in range(numOfBuckets):
        arr[i]=insertionSort(arr[i])
        k =0
        for i in range(numOfBuckets):
            for j in range(len(arr[i])):
                customlist[k]=arr[i]
                k+=1
        return customlist
        
        
def mergeSort(customlist, l, m, r):
    n1=m-l+1
    n2=r-m 
    L=[0]*(n1)
    R=[0]*(n1)
    for i in range(0, n1):
        L[i]=customlist[l+1]
    for i in range(0, n2):
        R[j]=customlist[m+1+j]
    
    i=0
    j=0
    k=l
    while i<n1 and j<n2:
        if L[i]<=R[j]:
            customlist[k]=L[i]
            i+=1
        else:
            customlist[k]=R
            j+=1
        k+=1
    while i<n1:
        customlist[k]=L[i]
        i+=1
        k+=1
    while i<n1:
        customlist[k]=R[j]
        j+=1
        k+=1        

def merge(customlist,l,r):
    if l<r:
        m=(l+(r-1))//2
        merge(customlist,l,m)
        merge(customlist,m+1,r)
        mergeSort(customlist,l,m,r)
    return customlist

def partition(customList,low,high):
    i=low-1
    pivot=customList[high]
    for j in range(low,high):
        if customList[j]<=pivot:
            i+=1
            customList[i], customList[j]=customList[j], customList[i]
    customList[i+1], customList[high]=customList[high], customList[i+1]
    return (i+1)

def quickSort(customlist, low, high):
    if low<high:
        pi=partition(customlist,low,high)
        quickSort(customlist, low, pi-1)
        quickSort(customlist, pi+1, high)
        
    

cList= [5419,41894,894,9845,41564,894,945691,984,89489,4894,894,8945,1894,489,4894,564,84894,894,8489,4,894,8,8,84894,5]
Bs(cList)